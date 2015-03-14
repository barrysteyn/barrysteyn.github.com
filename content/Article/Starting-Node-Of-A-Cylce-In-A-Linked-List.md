Date: 2015-02-18
Title: The Starting Node Of A Cycle In A Linked List
Tags: algorithms, math
Slug: Starting_Node_Of_A_Cycle_In_A_Linked_List

#Introduction
Given a [singly linked list](http://en.wikipedia.org/wiki/Linked_list#Singly_linked_list) that has a cycle, how can one determine the first node in the cycle?

<img src ="http://doctrina.org/images/ll-cycle-problem.png" />

Using the image above as an example, the aim would be to find the orange node.

#Algorithm
<img src ="http://doctrina.org/images/ll-cycle-intersection.png" />
Use two iterators, but make one move at twice the speed of the other. Starting from the head (first) node of the list, these iterators will meet at the red colored node. Now set one iterator back to the head node and leave the other at the red node. Moving both iterators at normal speed where they meet for the second time will be the orange node.

Go through this algorithm yourself with the above image, and it can easily be that the algorithm works for this example. Ever wondered why it worked? I did, but I never really thought of it until I was chatting to my colleague [Reza Jooyandeh](http://www.jooyandeh.com/). Reza immediately saw a nice way to prove this algorithm, I am just formalizing it here.

##History
This algorithm actually has a formal name: It is called [Floyd's cycle-finding algorithm](http://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare) and can be used to find cycles in a graph (a linked-list is also a graph) without using extra space in linear time. It is named after [Robert W. Floyd](http://en.wikipedia.org/wiki/Robert_W._Floyd).

#Proof Of The Algorithm
<img src ="http://doctrina.org/images/ll-cycle-definition.png" />

Assume the following (refer to the above image):

 * The node that starts the cycle is colored orange.
 * There are $X$ number of nodes up to and including the orange node.
 * The cycle contains $Y$ number of nodes where $Y \geq 2$ (since by definition, a cycle must contain at least two nodes).
 * The two iterators first meet after $Z$ nodes from the start of the cycle (these nodes are colored red in the above image).

##Aim Of The Proof
The aim is to prove that the starting node of the cycle will be reached after advancing $X$ number of nodes from where the iterators first meet ($Z$ nodes into the cycle). Why does this suffice? Because we assume that there are $X$ number of nodes leading up to the start of the cycle, so advancing $X$ number of nodes inside the cycle to get to the start implies that the two iterators will meet at the beginning of the cycle.

##Proof
The proof is done in two parts. It is proved that:

 1. The fast iterator cannot "jump" over the slow iterator in the cycle. 
 2. Advancing by $X$ nodes from $Z$ nodes into the cycle will yield the beginning of the cycle.

### The fast iterator cannot "jump" over the slow iterator in the cycle
This proved by contradiction. Assume the fast iterator will always jump over the slow iterator. Then if the slow iterator ends at position $(x+1)$, the fast iterator will end at $(x+2)$. But this can only happen if both iterators started at position $x$, which is a contracdiction.

This has three implications:

 1. The iterators will *always* meet in the cycle.
 2. The slow iterator cannot complete more than one cycle before the intersection occurs.
 3. By the above implication, this algorithm is linear in the number of nodes present: $O(n)$

 The second implication above may need some explaining. The cycle has $Y$ nodes, and while the slow iterator advances over those nodes, the fast iterator will catch up to it. As shown above, the fast iterator cannot jump over the slow iterator and therefore they will meet (I leave this as an exercise to the reader to prove more formally).

### Advancing by $X$ nodes from $Z$ nodes into the cycle will yield the beginning of the cycle.
To start the proof, note that the two iterators first meet after $Z$ nodes from the start of the cycle. The iterator that advances at normal speed would have progressed $X+Z$. The iterator that advances at double speed could potentially have gone round the cycle many times, so it would have progressed $X+n\cdot Y+Z$ nodes, where $n \in \mathbb{N}$. The proof starts by establishing a relationship between these iterators: The number of nodes progressed by the normal iterator at double speed (i.e. $2\cdot (X+Y)$) is equal to the number of nodes progressed by the fast iterator (i.e. $X+n\cdot Y+Z$).

\begin{array}{ll}
X+n\cdot Y+Z & = & 2\cdot (X+Z) \text{ where } n \in \mathbb{N} \\
Z+X & = & n\cdot Y \\
Z+X & = & 0\bmod Y \\
\end{array}
This proves that advancing by $X$ nodes from $Z$ will get to the start of the cylce.
