Date: 2013-03-16
Title: The Guiding Principles In Algorithm Analysis
Slug: The-Guiding-Principles-In-Algorithm-Analysis
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

# Guiding Principle 1: Worst Case Analysis
Why worst case analysis:

 1. Running time will hold for **every** input of length n.
 2. Very appropriate *general purpose* routines.
 3. Average case analysis requires *domain knowledge*.
 4. Worst case is usually much easier to analyse.

# Guiding Principle 2: Ignore constant factors and lower-order terms

 1. It is easier to analyse.
 2. Constants depend on computer architecture/compiler/programmer. Therefore it loses generality.
 3. Throwing away constant factors/lower-order terms loses very little predictive power.

# Guiding Principle 3: Asymptotic Analysis

Focus on running times for large input values. This is because only big problems are interesting (small problems can be solved in inefficient ways quickly).

Example: $\underbrace{6n\cdot log_2n+6n}_{\text{Merge Sort}} $ is better than $\frac{1}{2}\cdot n^2 $ (selection sort)

# A Fast Algorithm
A fast algorithm (using the above guiding principles) is therefore an algorithm that grows slowly in *worst case running time* when input grows.
