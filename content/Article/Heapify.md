Date: 2015-07-22
Title: Heapify Analysis
Slug: heapify-operation-analysis
Tags: datastructures, heap
Status: draft

# Introduction

# Background Knowledge

## Notation
I will use the following notation:

\begin{array}{ll}
h && \text{the height of node} \\
n && \text{the number of nodes in a tree} \\
\end{array}

## Tree Node Height
A tree node's height is the number of edges in the longest downward path between the node and a leaf[ref]A leaf is a node with no children.[/ref].

### Lemma: Maximum number of nodes of height $h$

## A Heap

 - Almost complete binary tree
 - Heap property: key[x] <= all keys of x's children
 - Implementation needs a random access list => array

### Heap Operations

 - calculate a node's parent
 - calculate a node's children
 - bubble down

# Heapify

## Algorithm

The heapify algorithm is extremely simple:

    Heap = arbitrary array
    idx = (Heap.size()-1)/2
    while (idx > 0)
       BubbleDown(idx)
       idx--

## Proof That Heapify Is Linear

First, an observation: In a binary tree, the number of nodes of a certain height
is less than or equal to $\left\lceil\frac{n}{2^{h+1}}$. Using ceilings is awkward,
and it can be removed by using $n+1$ in the numerator:

$$
\text{number of nodes of height }h \leq \frac{n+1}{2^{h+1}}
$$

The reason it works is because a full and complete binary tree is always odd, and
therefore, $2^{h+1}$ will never divide $n$. Adding $1$ to $n$ will make it even,
and therefore remove the need for the ceilings.

\begin{align*}
\text{Heapify for all }n\text{ nodes} & = \sum_{h=0}^{log_2n} n\cdot O(h) \\
                                      & \leq \sum_{h=0}^{log_2n} (n+1) \cdot O(h) \\
                                      & = \sum_{h=0}^{log_2n} (n+1)\cdot \frac{c\cdot h}{2^{h+1}} \\
                                      & = (n+1) \cdot \frac{c}{2}\cdot\sum_{h=0}^{log_2n}\cdot \frac{h}{2^h} \\
                                      & \leq (n+1) \cdot \frac{c}{2} \sum_{h=0}^\infty \cdot \frac{h}{2^h} \\
                                      & = (n+1) \cdot\frac{c}{2}\cdot d \\
                                      & = O(n+1) = O(n)
\end{align*}
