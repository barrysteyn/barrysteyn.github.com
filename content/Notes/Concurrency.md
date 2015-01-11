Date: 2013-04-22
Title: Concurrency
Slug: Concurrency
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Status: draft

Concurrency is very prone to error if not done correctly. Even things like AJAX, which do things asynchronously, may need to access data from other parts of a program.

#Threads

 * Is a fundamental unit of execution.
 * Every program has at least one thread running.
 * Each thread has its own stack and runs independently.
 * Threads share memory and data <= ***This is where the danger comes in**

##Access To Shared Data Needs To Be Controlled
A common side effect is data corruption.

###Monitors And Semaphores
Monitors and semaphores are *thread synchronization* mechanisms.

**Monitor** - a set of routines protected by a mutual exclusion lock. A thread must wait to execute routines in a monitor - meaning only one thread at a time can execute in a monitor. A thread can suspend itself in a monitor, thus giving up its lock.

**Semaphore** - more simple than a monitor: It is just a lock that protects shared resources. Examples are a *mutex*.

Monitors are much simpler to use because the sparse nature of semaphores. For example, using semaphores requires each thread to carefully release its thread (including in conditions where the thread ends unexpectedly) otherwise no other thread that needs the shared resources can begin. It also requires them to manage acquiring of locks. Monitors on the other hand handle this all automatically. 

###Deadlocks
This situation occurs when two threads block each other. For instance, two threads, A and B, are each waiting for a lock that the other has acquired. There is no suitable conflict resolution that is known. Some ideas are to always acquire locks in the same order, and release them in reverse order. 

##Native/Kernel-level Threads Vs Green Threads Vs User Threads
Native threads are started and managed by the Kernel. Green threads are started by a software layer above the kernel (e.g. a virtual machine). Green threads cannot take advantage of multi-core processors, and therefore there is a shift away from them.

Key concepts:

 * **Native Threads**
 * **Green Threads**  

##System Threads Vs User Threads
System threads are created by the **system** (OS). For instance, the first thread that is created when a program starts. The program often exits when this thread terminates.

User threads are created by an user application to perform tasks that should not be performed by the main thread. For example, the event loop is a user thread.

##Preemptive Threading
Due to finite resources, only a certain amount of threads can run concurrently any one time. The OS therefore gives each thread a window of execution time, after which it switches to another thread. It accomplishes this by pausing the current thread's execution and then switching to the new thread. This is **preemptive threading**.

Key concepts:
 
 * **preemptive threading** - 
 * **context switch** - the pausing and saving of thread state in order to switch to another thread.
 * **cooperative model** - the opposite of preemptive threading, where a thread will inform other threads when not busy so they can run

#Threading Examples In Java

In Java, use the `synchronized` keyword to make a monitor around routines.

#Common Synchronization Problems

##Busy Waiting
Busy waiting is when a thread is waiting for another thread to complete. The first thread is performing this wait by continually polling to see if the other thread is alive. Even though the waiting thread is not doing any work, because it is not sleeping, it is stealing resources.

Here is a simple example of *busy wait*:

    Thread task = new TheTask();
    task.start();
    while (task.isAlive()) {
        // do nothing
    }

This can be avoided by using a monitor or a semaphore

    class TheTask extends Thread {
        public void run() {
            synchronized(this) {
                //do something

                this.notify();
            }
        }
    }

    Thread task = new TheTask();
    synchronized(task) {
        task.start();
        try {
            task.wait();
        } catch (interruptedException e) {
            //do something if interrupted
        }
    }

##Producer/Consumer
This is a classic problem! The problem is to write a producer and consumer thread, where the producer produces numbers and the consumer consumes them.

    
    class BufferInt {
        private int size=0;
        public int[] buffer;
        public BufferInt(int size) {
            buffer = new int[size];
        }

        synchronized public void add(int num) {
            while (size >= buffer.length) {
                try {
                    wait();
                } catch (InterruptedException e) {
                }
            }

            buffer[size++] = num;

            notifyAll();
        }

        synchronized public int remove() {
            while (size==0) {
                try {
                    wait();
                } catch (InterruptedException e) {
                }
            }
            int ret = buffer[--size];
            notifyAll();
            return ret;
        }
    }

    public class Consume extends Thread {
        private BufferInt bint;

        public Consume(BufferInt bint) {
            this.bint = bint;
        }
    }

    public class Produce extends Thread {
        private BufferInt bint;

        public Produce(BufferInt bint) {
            this.bint = bint;
        }
    }
