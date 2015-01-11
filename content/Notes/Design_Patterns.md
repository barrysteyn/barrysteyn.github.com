Date: 2013-04-22
Title: Design Patterns
Slug: Design-Patterns
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Status: draft

#Design Patterns
The classic design pattern book is the [gang-of-four](http://en.wikipedia.org/wiki/Design_Patterns) book. Design patterns are simply guidelines for identifying and solving certain problems. They are abstract in nature, and hence are not implemented as a core language feature. Also, the word anti-pattern crops up: It is a pattern that is detrimental to the outcome of the task.

#Common Design Patterns

##Creational Patterns

###Singleton
A singleton patterns ensures at most one instance of any class is available at any one time. Applications cannot create a new instance of a singleton.

C++:

    class ClassicSingleton {
        protected:
            ClassicSingleton();
        public:
            static ClassicSingleton & getInstance();
            
    }

    ClassicSingleton& ClassicSingleton::getInstance() {
        static ClassicSingleton instance;
        return instance;
    }

Java:

    public class ClassicSingleton {
       private static ClassicSingleton instance = null;
       protected ClassicSingleton() {
          // Exists only to defeat instantiation.
       }
       public static ClassicSingleton getInstance() {
          if(instance == null) {
             instance = new ClassicSingleton();
          }
          return instance;
       }
    }

Note:

* That the constructor is protected. If the constructor is private, then inheritance is not possible.
* Lazy instantiation: Both the C++ and Java versions implement lazy instantiation, meaning that an instance is only produced when first needed.

###Builder
A builder pattern is used to create complex objects. Complex in this sense could be an object that has a very complex constructor:

Java:

    public class Complex {
        public Complex(int first, bool second, char third, int fourth, bool fifth, float sixth, bool seventh, bool eighth) {
        }
    }

    public class ComplexBuilder {
        public setFirst(int first) {...}
        ...
        public Complex Build() {
            return Complex(...);
        }
    }

###Factory Method
The factory method is a method that creates an object. Unlike the builder pattern, it is not a class. Technically, it can be any method that is used to create an object. It is used in conjunction with inheritance: A base class will define a factory method and **always** uses it to create objects. A derived class can inherit from the base class and can override the method.

The classic example (used in the GOF book) is a class that creates a two kinds of maze games:

    1. A normal maze game, where each room is connected to each other.
    2. A magic maze game, where each room is not only connected to each other, but it also has the ability to magically teleport.

    public class Maze {
        public createRoom() {
            return new ordinaryRoom();
        }

        public Maze() {
            room1 = createRoom();
            room2 = createRoom();
            room1.connect(room2);
        }
    }

    public class MagicMaze extends Maze {
        public createRoom() {
            return new magicRoom();
        }
    }

###Abstract Factory

##Behavioral Patterns
###Iterator
###Observer
