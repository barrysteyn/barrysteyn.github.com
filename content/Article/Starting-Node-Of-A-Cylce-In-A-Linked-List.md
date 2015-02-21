Date: 2015-02-18
Title: The Starting Node Of A Cycle In A Linked List
Tags: algorithms, math
Slug: Starting_Node_Of_A_Cycle_In_A_Linked_List
Status: draft

#Introduction
There is a classic algorithm interview question which states: 

> Given a [singly linked list](http://en.wikipedia.org/wiki/Linked_list#Singly_linked_list) that has a cycle, determine the first node in the cycle?

<img src ="http://doctrina.org/images/ll-cycle-problem.png" />

Using the image above as an example, the aim would be to find the orange node.

#Algorithm
<img src ="http://doctrina.org/images/ll-cycle-intersection.png" />
Refer to the above image in the explanation. Use two iterators both starting at the first node, but make one move at twice the speed of the other. These iterators will meet at the red colored node. Now set one iterator to the first node and leave the other at the red node. Moving both iterators at normal speed where they meet will be the orange node.

Go through this algorithm yourself with the above image, and it can easily be seen be seen that the algorithm works for this example. The remainder of this article proves mathematically that this algorithm will work for any cycle example.

Ever wondered why it worked? I did, but I never really thought of it until I was chatting to my colleague [Reza Jooyandeh](http://www.jooyandeh.info/). Reza immediately saw a nice way to explain and prove this, I am just formalizing it here.

##History
This algorithm actually has a formal name: It is called [Floyd's cycle-finding algorithm](http://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare) and can be used to find cycles in a graph (do note that a singly linked-list is also a graph) without using extra space. It is named after [Robert W. Floyd](http://en.wikipedia.org/wiki/Robert_W._Floyd) who was credited with it's invention by [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth)

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
To start the proof, note that the two iterators first meet after $Z$ nodes from the start of the cycle. The iterator that advances at normal speed would have progressed $X+Z$. The iterator that advances at double speed could potentially have gone round the cycle many times, so it would have progressed $X+n\cdot Y+Z$ nodes, where $n \in \mathbb{N}$. The proof starts by establishing a relationship between these iterators: The number of nodes progressed ny the normal iterator at double speed (i.e. $2\cdot (X+Y)$) is equal to the number of nodes progressed by the fast iterator (i.e. $X+n\cdot Y+Z$).

\begin{array}{ll}
X+n\cdot Y+Z & = & 2\cdot (X+Y) \text{ where } n \in \mathbb{N} \\
n\cdot Y & = & X+Z \\
n\cdot Y - Z & = & X \\
\end{array}
