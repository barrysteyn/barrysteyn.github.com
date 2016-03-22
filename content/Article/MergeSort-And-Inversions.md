Date: 2013-03-16
Title: Merge Sort And Inversions
Slug: Merge-Sort-And-Inversions
Author: Barry Steyn
Tags: Software, Computer Science, Algorithms

#Merge Sort
Merge sort is the classic divide and conquor algorithm, and is used as a canonical example for explaining the topic. It is quite easy to implement (specially in Python) but I wanted to see a C implementation. Google found me some [stack overflow](http://www.stackoverflow.com) links as well as several blog sites that listed code. And oh my god, the code was terrible. Most code that I have seen is a mixture of [Quick Sort](http://en.wikipedia.org/wiki/Quick_sort). And there are several untruths, for instance, that one can implement merge sort in place!

Merge sort is $O\left(n\cdot log(n)\right)$, and in fact, it is proven that for a comparison based sort, one cannot achieve better results. So then why is Quick Sort so popular when it is $O\left(n^2\right)$? It is because Quick Sort has average complexity of $O\left(n\cdot log(n)\right)$ (one has to choose very unlucky random pivots for it to be $O\left(n^2\right)$) but also, Quick Sort can be accomplished in *logarithmic space*. Merge Sort cannot! In fact, merge sort's space complexity is always going to be $2\cdot n$ - there is no getting around this and still guaranteeing $O\left(n\cdot log(n)\right)$ performance.

To Summarize:

 * Merge Sort time: $O(n\cdot log(n))$.
 * Merge Sort space: $O(n)$

## Merge Sort Example Code
Here is my C implementation of Merge Sort. The merge function is where the extra space is required, and although it is only required temporarily and destroyed once the stack is popped, it still makes the sort require $2\cdot n$ space.

<script src="https://gist.github.com/barrysteyn/5177637.js?file=mergesort.c"></script>

Note the following:

 * In line 2, a `temp` array is declared that is the size of the two merged subarrays combined. It is this array that makes Merge Sort not an *in place* sort.
 * In line 13, the `temp` array is copied back into the original array. There is no other way to achieve $O(n)$ complexity for this function unless a temp variable is used.

Why did I mention $O(n)$ in the above line when Merge Sort is $O(n\cdot log(n))$? It is because I am only referring to the merge function, which must be $O(n)$. The merge sort algorithm, being a binary divide and conquer, will run that merge function $log_2n$ times, giving Merge Sort worst case complexity of $O(n\cdot log(n))$.

It would be used like so:

<script src="https://gist.github.com/barrysteyn/5177637.js?file=main.c"></script>

#Counting Split Inversions
Merge sort leads to interesting applications besides sorting. One of the most interesting is counting the number of split inversions between two arrays. Assuming there are two arrays, the number of split inversions counts the number of swaps one array needs to transform into the other array. A *split inversion count* forms a [metric space](http://en.wikipedia.org/wiki/Metric_space) over the two arrays, and therefore one can accomplish measurements with it. For instance, one can use the inversion count as a metric for a recommender. How? If someone ranks movies from one to five, then that ranking can be compared to other rankings. One can then find similar rankings to note that these people have the same taste and therefore recommend movies that one person likes to the other.

##Counting Inversions: Brute Force
A brute force algorithm would be to compare each element in both arrays to each other, and determine if they would need to be swapped. This is $O(n^2)$ (quadratic in $n$). Can we do better?

##Counting Inversions: Divide And Conquer
In fact, we can do much better. The key point to note that is that we can get this information for free during the merge stage of the Merge Sort.

In the merge stage, two sorted arrays are merged into one sorted array. Lets call these arrays $A$ and $B$. Then the number of split inversions involving an element $y \in B$ of the second array is *precisely the number elements lefts in the first array $A$ when $y$ is copied into the temporary buffer*. Adding up these split inversions during the merge stage will result in the total number of split inversions.

<script src="https://gist.github.com/barrysteyn/5177637.js?file=merge-sort-with-split-inversion-count.c"></script>
