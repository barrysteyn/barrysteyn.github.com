Date: 2013-03-02
Title: Mathematical Nonsense - Inifinte Sum Series
Tags: Math, Mathematical_Nonsense
Slug: Mathematical_Nonsense_-Inifinite-Sum-Series
Category: Blog
Latex:

The following fact for infinite series crops up all the time:

$$ r\neq 1, 1+r+r^2+r^3+\ldots +r^k = \frac{r^{k+1}-1}{r-1} $$

#Proof
The proof is by induction:

###Base Case: k=1
For the base case, where k=1, the left hand side of the above sum is $1+r$, and the right hand side is $\frac{r^2-1}{1-r}$:

\begin{aligned}
 1+r &= (1+r)\cdot \frac{1-r}{1-r} \cr
 &= \frac{(1+r)(1-r)}{1-r} \cr
 &= \frac{r^2-1}{1-r} \cr
\end{aligned}

###Inductive Case: k=n
Assume the above holds for $k=n-1$, then $1+r+r^2+r^3+\ldots +r^{n-1} = \frac{r^n-1}{r-1}$. 

$$\left( 1+r+r^2+r^3+\ldots +r^{n-1} \right) + r^n $$

By the inductive argument:

\begin{aligned}
 &= \frac{r^n-1}{r-1} + r^n \cr
 &= \frac{r^n\cdot(r-1)+r^n-1}{r-1} \cr
 &= \frac{r^{n+1} - r^n + r^n -1}{r-1} \cr
 &= \frac{r^{n+1} -1}{r-1} \cr
\end{aligned}

#Some useful facts

###Assume r < 1, then the sum is bounded by $\frac{1}{1-r}$
If $r < 1$, then: $1+r+r^2+r^3+\ldots +r^k \leq \frac{1}{1-r}$

This is easy to see: if $r<1$, then $1 - r^{k+1} \leq 1$, and so $\frac{r^{k+1}-1}{r-1} = \frac{1-r^{k+1}}{1-r}\leq \frac{1}{1-r}$.

In this case, the series sum is dominated by the first term (e.g. 1), and is bounded above by something that is independent of k.

###Assume r > 1, then the sum is bounded by $r^k\cdot \left(1+\frac{1}{r-1} \right)$
If $r > 1$, then: $ 1+r+r^2+r^3+\ldots +r^k \leq r^k\cdot \left(1+\frac{1}{r-1} \right)$

The proof:
\begin{aligned}
 \frac{r^{k+1}-1}{r-1} &\leq \frac{r^{k+1}+1}{r-1}\cr
 &= \frac{r^{k+1}}{r-1} + \frac{1}{r-1} \cr
 &= r^k\cdot \frac{r}{r-1} + \frac{1}{r-1} \cr
 &\leq r^k + \frac{1}{r-1} \cr
 &\leq r^k + \frac{r^k}{r-1} \cr
 &= r^k \cdot \left(1 + \frac{1}{r-1} \right) \cr
\end{aligned}

In this case, the series sum is dominated by the last term (e.g. $r^k$), and is bounded above by $2\cdot r^k$.
