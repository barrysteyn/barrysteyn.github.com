Date: 2012-10-12
Title: Algorithm Analysis:How It Works With Examples
Tags: theory
Slug: Algorithm-Analysis-How-It-Works-With-Examples
Status: draft

Algorithm analysis is the science (or art) of measuring comparable efficiencies of algorithm. It provides a theoretical reason why [bubble sort]() is not very popular while [quick sort]() is. Devices that run algorithms have neither infinite storage/memory space nor infinite processing power. Due to these limitation, it becomes necessary to provide a metric that will relate an algorithm's input length to the number of processing steps or storage space needed. Algorithm analysis provides this metric.

##Assymptotic
Algorithm analysis is measured asymptoticly meaning that measurements apply to an arbitrary large input. Asymptotic measurements are vital to algorithm analyis because different implementations of an algorithm may differ in efficiency when using small inputs. However the efficienies of any two *reasonable* algorithms are comparable when using arbitrary large input values. This is the reason why implementations of *bubble sorts* are always comparable with asympotic notation, no matter the efficiency gain one can get from tweaking the algorithm.

##Big O Notation
Big O (pronounced big Oh) is the most commonly used asymptotic notation in algorithm analysis. Its symbol is $O$ and it describes a *worst case* performance that an algorithm could attain given an arbitrary large input. Since $O$ measures *worst case*, it is an upper bound: If an algorithm is considered $O(g(n))$, it means that the worst case performance of that algorithm is *at least less than or equal* to $g(n)$.

##How Did These Notations Come About
Computer science was originally a branch of Mathematics. The founding fathers of Computer Science ([Alan Turing](), [John von Neuman]() etc) were mathematicians. In addition, [Donald Knuth](), the person who some consider the greatest living Computer Scientist, is first and foremost a mathemetician. These people have used math to both invent the computer and algorithms. So it was natural that these people would use a branch of math to forumlate a metric for an algorithm's efficiency.

#Mathematical Background
A mathematical function $f(n)$ is equal to $O(g(n))$ if there exists constants $c > 0,n_0 > 0$ such that $0 \leq f(n) \leq c\cdot g(n)$ for all $n \geq n_0$. Stating this again for emphasis:
\begin{equation}
	\label{BIGODEF} f(n) = O(g(n)) \implies 0 \leq f(n) \leq c\cdot g(n) \forall n \geq n_0, c,n_0 \in \mathbb{N}
\end{equation}

For example, $2n^2 = O(n^3)$, because by setting $c=1,n_0=2$, $0 \leq 2n^2 \leq n^3$. In this instant, $2n^2$ is also equal to $O(n^4)$. While this is confusing to algorithm analysis, it does make sense: Big O is an upper bound, but it is not the least upper bound, therefore any upper bound will apply to Big O. However, in algorithm analysis, it is normally taken for granted that the Big O of an algorithm is the least upper bound (anything else would not make much sense).

##Warning: Big O Is Not A Symmetric Relationship
Normally when two variables are equal, it is a symmetric relationship. For example, if $a=b$, then $b=a$. This is not the case for Big O!

When one writes: $f(n) = O(g(n))$, it does not mean that $O(g(n)) = f(n)$. This asymmetry is quite confusing, and to lessen confusion, we really shouldn't be using the $=$ sign which is commonly used in symmetric relationships. What is really meant when one writes $f(n) = O(g(n))$ is that $f(n)$ is an element of the set $O(g(n))$: $f(n) \in O(g(n))$. $O(g(n))$ is a set that holds functions which obey the equation $\ref{BIGODEF}$, and therefore $O(g(n)) \neq f(n)$.

To recap: $fn = O(g(n))$ does not mean that $O(g(n)) = f(n)$. Confusion can now be avoided.

#Algorithm Analysis: How It Works
##Algorithms
The following algorithms will be used to explain examples of $O$ efficiency:

1. Array look up given an index: Will be used to explain *constant* efficiency
2. Array search in an unordered array: Will be used to explain *linear* efficiency
3. Binary tree search: Will be used to explain *logarithmic* efficiency.
4. Bubble sort: Will be used to explain *quadratic* efficiency.
5. The travelling salesperson problem: 

###Array lookup given an index
An array lookup (via an index into the array) takes a constant time, no matter the size or the element that is accessed. An array is a *contiguous* piece equally sized memory. The variable that stores the array points to where the array begins. Accessing an element in the array via an index only requires a simple calculation: The array index multiplied by the space each portion of the array takes up and then added to the original memory address. If $a$ is the start memory address, $b$ is the size of each data structure in the array and $i$ is the index being accessed, then the element's address in the array is calculated like so:
\begin{equation}
    (b\times i) + a
\end{equation}

Obtaining an element given an index always takes the *same constant amount of time* defined by the above formula, no matter the array size of element being accessed. Therefore an array lookup via an index is $O(1)$ and has the following implications:

1. The algorithm's performance is independent from its input size.
2. $O(1)$ has no growth curve, in other words, efficiency of functions that belong to $O(1)$ are not affected as input size grows towards infinity.
3. There is *no* notion of $O(2), O(3),...,O(c)$ where $c \in \mathbb{N}_{> 0}$. Equation $\ref{BIGODEF}$ implies that if a function is $f$ is in $O(c), c \in \mathbb{N}_{> 0}$, then it is also an element of $O(1)$. Therefore, we make life easier by only using $O(1)$.

Constant efficiency is not really interesting in algorithm analysis due to the fact that $O(1)$ algorithms do not accomplish complex things.

###Binary Search
Binary search is a *divide and conquor* algorithm. Given an item to be searched for, decide if 

###Linear Search
A linear search involves searching through a list of items for a specific item. Since the position of the desired item is not known, it involves examining each item from start to finish. Assuming the list contains $n$ items, the worst case scenario involves examining each of those $n$ items. Therefore a linear search is $O(n)$.

###Bubble Sort
There are many ways to sort a list of integers. Bubble sort is one such way, but due to its terrible performance, it is not used in practice. A bubble sort involves comparing each item of a list to every other item. During comparison, if the item compared is smaller, then a swap is intiated (this will sort in ascending order).


#Algorithm Comparison

#Conclusion


#A Feel For Big O Notation
What does it mean for an algorithm to equal $O$ of something? Assume the following:

1. Constant: $O(1)$
2. Polynomial in $n$: $O(n)$
3. Polynomial in $n^2$: $O(n^2)$
4. Exponential $O(2^n)$

###Constant
An algorithm that is classified as $O(1)$ means that its worst case performance will always be less than or equal to $1$. This could perhaps be representing an internal operation of the CPU that takes this amount of time (for instance, adding two numbers). A constant $O$ is never represented with a specific number. The way that $O$ is mathematically defined (see below), all constants are equal in $O$. For instance, if an algorithm $f$ is equal to $O(1)$, then it is also equal to $O(2),O(3),...O(c)$ where $c$ is a constant. For algorithm analysis, this makes sense. If an algorithm's efficiency can represented by a constant, then the important thing to note is not how big the constant is, but that it is a constant. Computers are getting faster all the time; if an algorithm is $O(10^6)$, this might seem slow, but if Google's pagerank algorithm for the entire web was represented with $O(10^6)$, it would be extremely efficient. 

If an algorithm's efficiency is ...

###Polynomial in n

###Polynomial in $n^2$

###Exponential
 - describe here what it means for something to be O(n), O(n2), O(2^n)

#Background Mathematics
A formal definition for $f(n) = O(g(n)$ is as follows:

\begin{equation}
	f(n) = O(g(n)) \implies \exists c > 0, n_0 > 0 s.t 0 
\end{equation}

#Algorithms To Analyse
The following algorithms will be analysed:

1. Bubble Sort
2. Quick Sort

##Bubble Sort
##Quick Sort


#Conclusion
