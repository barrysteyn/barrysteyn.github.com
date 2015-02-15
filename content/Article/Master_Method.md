Date: 2013-02-27
Title: The Master Method
Slug: The-Master-Method
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms

#The Master Method
The master method is a way to analyse the worst case running times of a recursive function. Assume the recursive function is of the following form:

$$ T(n) = a\cdot T\left(\frac{n}{b}\right) + O(n)^d$$

Where:

 * **a** is the number of subproblems created. <u>Known as the *rate of subproblem proliferation* (RSP).</u>
 * **b** is the constant dividing factor that controls the size of each subproblem's input. <u>Known as the rate of work shrinkage (RWS).</u>
 * **d** is the exponent for the amount of work done on each recursive level.

Then

$$ T(n) = \begin{cases} O(n^d\cdot log n) & \text{if}\ a = b^d\ \text{case 1} \cr O(n^d) & \text{if}\ a < b^d\ \text{case 2}\cr O(n^{log_ba}) & \text{if}\ a > b^d\ \text{case 3}\end{cases}$$

##Canonical Example: Merge Sort
Merge sort is the classic divide-and-conquer algorithm. It is a comparison based sort that achieves the best time possible for comparison base sorts: $O(n\cdot log(n))$. For merge sort, the recursive function would be the following:
$$ T(n) = 2\cdot T\left(\frac{n}{2}\right) + O(n)$$ To spell things out:

 * **a** is 2. Merge sort divides its input into two, and then recursively works on each sub problem. Therefore there are two sub problems and hence a=2.
 * **b** is 2. Each subproblem's input is divided by 2, hence b=2.
 * **d** is 1. This is the work done at each level after the recursive calls. For merge sort, the work is merging each of the two $\frac{n}{2}$ input of the subproblem.

It is easy to see via a recursion tree that Merge sort takes $O(n\cdot logn)$ time. The master method totally agrees with this, as merge sort falls into case 1, with $a=2$, $b=2$ and $d=1$.

##The Work Done At Each Level
At any level $j$ in the recursive subtree, there are $a^j$ subproblems of size $\frac{n}{b^j}$. Therefore at any one particular level, the work at level $j$ is: 
\begin{equation}
\text{Work done at level j} \leq a^j \cdot c\cdot \left( \frac{n}{b^j} \right)^d = c\cdot n^d \left(\frac{a}{b^d}\right)^j \label{wdael}
\end{equation}

##Total Work Done
At any recursion tree, the leaves are at level $log_b(n)$, where *b* is the rate of work shrinkage. The merge sort canonical example demonstrates this - *b* is 2 (problem is halved at each level of the recursion tree), and so there are $log_2(n)$ before the leaves are hit.

If the work done at each level is dominated by inequality $\ref{wdael}$, then the total work done is the sum of up to $log_b(n)$:
\begin{equation}
\text{Total work done} \leq c\cdot n^d \sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j \label{twd}
\end{equation}

### Intuition For The Three Cases
When the master method was first explained to me, my lecturer humorously called the rate of work shrinkage (RWS - denoted by *b*) the *"force of good"* and the rate of subproblem proliferation (RSP - denoted by *a*) the *"force of evil"*. The following paragraphs perhaps explain this humour.

####RWS = RSP
When rate of work shrinkage is equal to rate of subproblem proliferation, then the same amount of work is being done for each level of the recursion. Therefore work done is calculated by multiplying the number of levels by the work done at every level (Case 1: $O(n^d\cdot log(n))$).

Again, the canonical merge sort example: There are $log_2n$ levels, with each level doing $O(n)$ work. Therefore total is $n\cdot log(n)$.

####RWS > RSP
When rate of work shrinkage is greater than rate of subproblem proliferation, then work done is *decreasing* at each level (btw: This is very rare but when it happens is very good). Work done will therefore be dominated by the root of the recursion tree (Case 2: $O(n^d)$).

####RWS < RSP
When rate of work shrinkage is less than rate of subproblem proliferation, work is *increasing* at each level of the recursion. Work done will therefore be dominated by the leaves of the recursion tree (Case 3: expect O(#number of leaves)).

#Master Method Proof
##Lemma
The following lemma will help with the proof.

For $r \neq 1$:

$$ 1 + r + r^2 + r^3 + \ldots + r^k = \frac{r^{k+1}-1}{r-1}$$

The above can be proved by induction, and [I have done this just](http://doctrina.org/Mathematical_Nonsense_-Inifinite-Sum-Series.html) for fun. From the above, two facts follow:

 1. If $r < 1$, then the sum is bounded above by $\frac{1}{1-r}$. This means that the first term in the sum is the dominant term. Therefore the sum can be bounded above by some constant.
 2. If $r > 1$, then the sum is bounded above bt $r^k\cdot\left(1 + \frac{1}{1-r} \right)$. This means that the last term (i.e. $r^k$) is the dominant term, and in fact, the sum will always be less then $2\cdot r^k$.

##Proof For Case 1
Assume $a=b^d$, then $\left(\frac{a}{b^d}\right) = 1$, and so $\sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j = log_b(n) + 1$. With this in mind: $c\cdot n^d \sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j = c\cdot n^d \cdot log_b(n) + 1 = O(n^d\cdot log n)$.

##Proof For Case 2
If $a < b^d$, then $\left(\frac{a}{b^d}\right) < 1$. This is where the above lemma comes into play, because $\sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j \leq f$. Why do I use the constant *f*? It is because in the lemma above, there is a constant that will always be greater than $\frac{1}{1-r}$ if $r < 1$. Therefore $c\cdot n^d \sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j \leq f\cdot c\cdot n^d = O(n^d)$.

##Proof For Case 3
Before I begin the proof for case 3, in a recursion tree, how many leaves are there? The answer: $a^{log_bn}$. This is because there are $log_b(n)$ levels in the recursion tree, with each level splitting into *a* subproblems.

If $a > b^d$, then $\left(\frac{a}{b^d}\right) > 1$. Again, the above lemma comes into play: $\sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j \leq 2\cdot \left(\frac{a}{b^d}\right)^{log_bn}$. Therefore $c\cdot n^d \sum_{j=0}^{log_bn} \left(\frac{a}{b^d}\right)^j \leq 2\cdot c\cdot n^d \cdot \left(\frac{a}{b^d}\right)^{log_bn}$. Note that $b^{-dlog_bn} = \left(b^{log_bn}\right)^{-d} = n^{-d}$. So $2\cdot c\cdot n^d \cdot \left(\frac{a}{b^d}\right)^{log_bn} = 2\cdot c\cdot a^{log_bn} = O(a^{log_bn})$. As shown above, this is the number of recursion leaves.

The more astute of you out there may notice that *case 3* was presented as $O(n^{log_ba})$. This is because $n^{log_ba} = a^{log_bn}$ (I did not believe this at first, and had to [prove](http://doctrina.org/Mathematical_Nonsense_Lemma-For-Logarithm-Equality.html) it to myself). Even though it is more intuitive to understand $a^{log_bn}$ (i.e. the leaves of the recursion sub tree), it is more consistent with the other cases to calculate $n^{log_ba}$.
