Date: 2015-05-11
Title: Maximum Height Of A Red-Black Tree
Slug: maximum-height-of-red-black-tree
Tags: datastructures, red-black tree

# Introduction
My friend and colleague, [Dominik Messinger](http://dome.hobbits.grus.uberspace.de/) was fortunate to learn about abstract data structures in high school[ref]He is German, so I think this is a nod to the excellent school system in Germany.[/ref]. After chatting to him one day, the topic of red-black trees came up. He studied [AVL trees](http://en.wikipedia.org/wiki/AVL_tree) in depth at high school, but did not do the same for red-black trees. After this chat, I realized I had not formalized this topic in my mind either. So I decided to choose one topic and write about...

So here is an analysis of the maximum height of a red-black trees.

# Background Knowledge

## Tree Node Depth

A tree node's depth is the number of parent node ancestors the node has. Depth is zero based (the root is at depth 0 since it has no ancestors).

{% img images/binary-tree-depth.png %}

The number of nodes in a path from the root node to a node at depth $k$ is $k+1$. For example:

 * **At depth 0**: There is 1 node in the path from root to depth 0 (the root node).
 * **At depth 1**: There are two nodes in a path from root to depth 1.
 * **At depth $k$**: There are $k+1$ nodes in a path from root to depth $k$.

## Full And Complete Binary Tree
A tree that is both *full and complete*[ref]Full and complete binary trees are sometimes called *perfect binary trees*.[/ref] has the following properties:

 1. All non-leaf nodes have two children.
 2. All leaf nodes are at the same depth.

{% img images/full-complete-binary-tree.png %}

A full and complete binary tree with $n$ nodes and maximum depth $k$ (the depth of the leaf nodes) has the following relationship:
\begin{equation*}
n = 2^{k+1}-1
\end{equation*}

# Red-Black Tree
## Red-Black Tree Invariants
A red-black tree is a [binary search tree](http://en.wikipedia.org/wiki/Binary_search_tree) that is constrained by the following 4 invariants:

  1. Each node is either red or black.
  2. The root node is black.
  3. Every red node must either have zero or two black chilren.
  4. Every root-null path must have the same number of black nodes.

### The Maximum Depth Of A Red-Black Tree
The maximum depth of a red-black tree is the root-null path that contains the most number of nodes. Ironically, an examination of the shortest root-null path (the root-null path with the least number of nodes) is needed to calculate the maximum depth.

#### Length Of The Shortest Root-Null Path
By invariant 4, the *maximum number of black nodes* in any root-null path is restricted by the number of nodes in the *shortest* root-null path. Assume the shortest root-null path has depth $k$:

 * There are $k+1$ nodes in the root-null path at depth $k$.
 * There is a *full* and *complete* binary subtree of depth $k$.

For example, if the shortest root-null path is at depth 2, the full and complete binary subtree would look like the image below:

{% img images/full-complete-binary-subtree.png %}

Suppose the full and complete binary subtree has $n$ nodes, then using the fact that $n=2^{k+1}-1$, the number of nodes in the root-null path (i.e. $k+1$) is logarithmic in $n$:

\begin{array}{ccc}
n & = & 2^{k+1}-1 \\
k+1 & = & \log_2(n+1)
\end{array}

*Due to invariant 4*, the maximum number of **black nodes** in any root-null path is $\log_2(n+1)$

#### Length Of The Longest Root-Null Path
The longest root-null path will have $\log_2(n+1)$ black nodes (the maximum that it can have due to invariant 4). The question now becomes: How many red nodes can be present? By invariant 3, a red node must have black node children. This restricts the maximum number of red nodes to being placed between the black nodes:

{% img images/red-black-in-between.png %}

The maximum number of red nodes in a root-null path is therefore constrained by the maximum number of black nodes, which is $\log_2(n+1)$. So the length of the longest root-null path is:

\begin{array}{lcl}
\text{Maximum height} &=& \text{max black nodes} + \text{max red nodes} \\
					  &=& \log_2(n+1) + \log_2(n+1) \\
					  &=& 2\cdot\log_2(n+1)
\end{array}

This proves that the height of a red-black tree is $O\left(\log n\right)$ where $n$ is the total number of nodes. It is also worth noting that the constant factor in the big-O notation is $2$, which is very low.

## Searching Is Logarithmic
In a binary search tree, the time complexity of a search operation is governed by the maximum height of the tree. This means that search in a red-black tree is logarithmic time complexity.

# Conclusion
A red-black tree is probably the most used balanced binary search tree algorithm. It is a little bit more work to show that *update*, *delete* and *insert* is also logarithmic, but any proof would rely upon the fact the maximum height is logarithmic.
