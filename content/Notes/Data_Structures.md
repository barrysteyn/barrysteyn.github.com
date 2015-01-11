Date: 2013-04-17
Title: Data Structures
Slug: Data-Structures
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

# Containers And Abstract Data Types

Data structures store data. They come in two flavours:

1. Storage and/or retrieval is independent of underlying data - known as a **container**
2. Storage and/or retrieval requires knowledge of underlying data

###Canonical Examples Of Containers
A *stack* is a container. A stack produces the last data item that was *pushed* onto it. No knowledge of this data item is needed.

**More Examples**: Queue, Priority Queue

###Canonical Examples Of Things That Are Not Containers
An *array* is not an example of an abstract data type. An array requires the index of the data item of interest in order to retrieve it.

**More Examples**: Dictionary, Binary Tree, Graph, Heap

Note: Heap and Priority Queue are very interesting. They are mostly considered the same thing, but if we have to really discern, a Heap is an abstract data type while a priority queue is a container.

# Dictionaries
A dictionary is an abstract data type that will ???

**Canoncial Example**: Hash Table.
A binary tree could also be an example of a dictionary

#Binary Tree
A node with left and right pointers. Optional parent pointer. Post/Pre-Order traversal make little sense with Binary Search Trees but can be useful when representing arithmetic or logical operations


