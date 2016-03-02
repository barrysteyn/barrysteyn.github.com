Title: Big O Notation
Date: 2016-02-03

# Introduction
{% youtube eNsKNfFUqFo %}

# Definition
Big O notation concerns functions **defined on the positive integers**:
A function $T(n)$ is said to be *big O* of $f(n)$ if eventually,
(*for all sufficiently large values of $n$*), $T(n)$ is bounded above
by a *constant multiple* of $f(n)$

## Formal Mathematical Definition
$$
T(n) = O(f(n)) \iff \exists \text{ constants } c, n_0 \text { s.t. } T(n) \leq c\cdot f(n)\hspace{2mm} \forall n \geq n_0
$$

# Orders Of Common functions
This taken from the [wikipedia article](https://en.wikipedia.org/wiki/Big_O_notation#Orders_of_common_functions)
about Big O.

The following list is in ascending order of growth:

 1. $O(1)$ - **constant** - array lookup by index
 2. $O(\log\log n)$ - **double logarithmic** - interpolation search
 3. $O(\log n)$ - logarithm - [Binary Search](../binary-search.html)
