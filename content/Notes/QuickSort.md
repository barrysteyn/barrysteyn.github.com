Date: 2013-03-16
Title: Quick Sort 
Slug: Quick-Sort
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

#Quick Sort
Quick sort will order an an array in-place with average time of $O(\codt log\cdot n)$. However, it does have worst case time of $O(n^2)$ yet it is very unusual to get this time as one has to make a pathalogical choice of pivots to achieve this.

##Code

##How It Works
Quick sort is a randomised algorithm meaning it picks a random element to pivot against. Once that element has been chosen, a partition function is called, which puts all elements less than the pivot on the left of the array, and all elements greater than the pivot on the right of the array. The result is that the pivot is perfectly in place in the final ordered array, yet the left and right sub arrays may not be ordered. So quick sort recursively sorts these sub arrays by picking pivots and partitioning on those pivots in those sub arrays.

# Proof Of Correctness
The proof is accomplished by induction:

### Base Case: Where n = 1
When $n=1$, the array is already ordered since there is only one element. In this case, quick sort returns this array hence it returns an ordered array.

### Inductive Case: Assume Quick Sort Produces Correctly Sorted Array Of Size $k$, Where $k < n$
A pivot is randomly selected and partitioned. After partitioning, the pivot is in place in the final ordered array, and sub-divides the array into a left and right array, each smaller than $n$. Because we assume that Quick Sort produces correctly sorted results of less than size $n$, the left and right sub arrays will be correctly ordered.

# Proof That Quick Sort Takes $O(\codt log\cdot n)$ Average Time To Run

