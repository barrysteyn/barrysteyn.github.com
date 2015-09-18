Date: 2015-09-17
Title: Maximum Amount Of Nodes Of A Certain Height
Slug: nodes-of-certain-height
Tags: datastructures, heap

# Introduction
Given a binary tree with $n$ nodes, there can be at most $\left\lceil \frac{n}{2^{h+1}} \right\rceil$ nodes with height $h$. Here follows a proof[ref]This proof is not my own, I found the main ideas by doing a Google Search. Unfortunately, I cannot find who to acknowledge, so if this looks familiar, please shout[/ref].

# Background Knowledge

## Tree Height
In a binary tree, *height* of a node is defined as the number of edges in *the longest path* from that node to a leaf node. Leaf nodes are therefore at height 0, while the root node has the largest height

## Max Number Of Leaves
For for a tree with $n$ nodes, there can be at most $\left\lceil\frac{n}{2}\right\rceil$ *leaf nodes*.

## Notation

The following notation will be used:

\begin{array}{lcl}
T & := & \text{tree of height } h \\
T^{'} & := & \text{tree of height } h-1 \\
n & := & \text{the number of nodes in } T \\
n^{'} & := & \text{the number of nodes in } T^{'} \\
N_h & := & \text{number of nodes of height }h\text{ in }T \\
N^{'}_{h-1} & := & \text{number of nodes of height }h-1\text{ in }T^{'}
\end{array}

# Proof

This is an inductive proof.

## Base Case
At height 0, there is only 1 node in the tree, namely the root node:

\begin{array}{lcl}
 N_0 & = & 1 \\
     & = & \left\lceil\frac{1}{2}\right\rceil \\
     & = & \left\lceil\frac{n}{2^{h+1}}\right\rceil
\end{array}

## Inductive Case

Assume that the relationship holds for height $h-1$.

**Note** that nodes at height $h$ in $T$ are at height $h-1$ in $T^{'}$. The number
of nodes in $T^{'}$, namely $n^{'}$, is equal to the number of nodes in $T$ minus
the leaf nodes in $T$:

$$
n^{'} = n - \left\lceil \frac{n}{2} \right\rceil  = \left\lfloor \frac{n}{2} \right\rfloor
$$

By induction:
\begin{array}{lcl}
  N_h & = & N^{'}_{h-1} \\
      & = & \left\lceil \frac{n^{'}}{2^h} \right\rceil \\
      & = & \left\lceil\frac{\left\lfloor \frac{n}{2}\right\rfloor}{2^h}\right\rceil \\
      & \leq & \left\lceil\frac{\frac{n}{2}}{2^h}\right\rceil \\
      & = & \left\lceil \frac{n}{2^{h+1}} \right\rceil
\end{array}
