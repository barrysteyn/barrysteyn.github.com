Date: 2013-04-11
Title: Algorithm Analysis
Slug: Algorithm-Analysis
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

# Algorithm Analysis

## Aymptotic Notation: Big Oh
Note: These definitions are not rigorous but should serve for interview purposes

 * $f(n) = O(g(n)) \Rightarrow f(n) \text{ is bounded above by } g(n)$ 
    * $f(n) \leq c\cdot g(n) \text{ for some constant } c$
 * $f(n) = \Omega(g(n)) \Rightarrow f(n) \text{ is bounded below by } g(n)$
    * $f(n) \geq c\cdot g(n) \text{ for some constant } c$
 * $f(n) = \Theta(g(n)) \Rightarrow f(n) \text{ is bounded above and below by } g(n)$ 
    * $c_0\cdot g(n) \leq f(n) \leq c_1\cdot g(n) \text{ for constants } c_0, c_1$

### Example
Is $(x + y)^2 = O(x^2 + y^2)$?

Expand $(x + y)^2$ to $x^2 + 2xy + y^2$, which contains an extra term, namely $2xy$. There are two scenarios: $x < y$ or $y < x$. In either case, $2xy \leq 2(x^2 + y^2)$. So $(x + y)^2 \leq 3\cdot (x^2 + y^2) \Rightarrow (x + y)^2 = O(x^2 + y^2)$.

##Growth Rates
Important to know that:

<center> $n! \gg 2^n \gg n^3 \gg n^2 \gg n\cdot log n \gg n \gg log n \gg 1$</center>

###Example of $n!$

###Example of $2^n$
A recursive definition of the Fibonacci series as presented below:
<script src="https://gist.github.com/barrysteyn/5413430.js"></script>
Note: There are more efficient ways of calculating Fibonacci series.

###Example of $n^3$

###Example of $n^2$

###Example of $n\cdot log n$
The canonical example is [Merge Sort]()

###Example of $n$

###Example of $log n$
Binary search.

###Example of $1$
Array index access.
