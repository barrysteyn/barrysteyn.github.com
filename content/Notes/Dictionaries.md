Date: 2013-04-22
Title: Dictionaries
Slug: Dictionaries
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

A Dictionary is a very useful data-structure to maintain a possibly evolving set of *"stuff"*. Dictionaries have three supported operations:

 1. Insert
 2. Delete
 3. Lookup

Dictionaries are distinguished by using *keys* as index values for the above operations.

#Hash Tables
Hash tables are the most famous form of a dictionary. It is based on an array and exploits the ability of array random access. 

Hash tables guarantee that *insertion*, *deletion* and *lookup* will all happen in O(1) time with the following caveats:

 1. The hash table must be properly implemented.
 2. The data must be non-pathological

**Key Concepts**:

 * Based on an array
 * Exploits random access property of an array

## Applications

###De-Duplication
Removes duplicates. In a stream of objects, use a hash-table to remove duplicates.

###2 Sum Problem

**input**: Integer list in *no-particular order*. A target sum *t*.
You need to find two integers from the unsorted list, *x* and *y* that sum to *t*.

**Solution**: Add each element to a hash table. Then, for each element *x*, search for *t-x* in the hash table.

###More examples

 1. **Compilers**. To support super fast lookups to for symbols.
 2. **Block network traffic**. Have a blacklist to drop things.
 3. **Speed up search algorithms**. Use hash table to avoid looking up things you have already looked up.

## Hash Implementation

 1. Choose size of array (the number of buckets)
 2. A hash function, which maps a key to a bucket.

What do when a **collision happens**. Two solutions:

 1. **Separate chaining**. Each bucket contains a linked-list, in which case, insert, delete and lookup is done on the list.
 2. **Open addressing**. If collision occurs, we probe the table in some other location. Therefore hash function produces hash sequence. There are various strategies: (1) Linear probing (2) double hash function.

Open addressing is more difficult to implement deletion.

###Properties of a good hash function

 1. It should lead to good performance. This is done by spreading data out as evenly as possible.
 2. It is important that the hash function can be evaluated quickly.

The gold standard would be a completely random function.

Hash functions are really easy to implement *badly*. With this in mind, here is a quick and dirty hash function that should produce acceptable results:

 * Choose *n* (the number of buckets) as a prime number.
 * The prime should not be too close to *patterns* in the data.

###Universal Hashing Function - Introduction
The load factor $\alpha$ of a hash table:

$$\alpha = \frac{\text{# of objects in a hash table}}{\text{# of buckets}}$$

The load needs to be constant $O(1)$ to run in constant time. For *open addressing*, the load must be less than 1, but even for *chaining*, the load better not much bigger than a factor of 1.

A perfect hash function cannot exist! This is because for every hash function, there is a pathological data that will make the function perform badly. This is because of the compression property of the hash function: By the pidgeon principle, there will always be data clashes.

**How to address the fact that a hash function always has a patholgical data set**:

 1. Use a cryptographic hash function - but it is slow. This is good because it is difficult to figure out the pathological data set
 2. Use randomization. Design a family of hash functions and then pick one at run time at random.

2 above implies that for each data set, choosing a random hash function will make it difficult to find the pathological data set to destroy the function.

###Universal Hash Function - Implementation

Let $H$ be a set of hash functions from $u$ to $\{0,1,2,\ldots,n-1\}$. $H$ is universal $\Leftrightarrow$ $\forall x,y \in u$, pr that $h(x) = h(y)$ is $\frac{1}{n}$ where $h \in H$.

**Example**: Creating a universal hash function for ip addresses.

 1. Ip addresses of the form $\(x_0, x_1, x_2, x_3\)$ where $x_n \in \{ 0,1,\ldots,256 \}$.
 2. Choose $n$ to be a prime number that that is some small multiple of the number of objects you want to store. For example, assuming you want to store 500 object, then $n$ can be 997.
 3. Choose a random 4-tuple $\(a_0, a_1, a_2, a_3\)$ where $a_n \in \{0, 1, 2, \ldots, n-1\}$.
 4. Define a set of hash functions $h_a\(x_0, x_1, x_2, x_3\) = \left(a_0\cdot x_0+a_1\cdot x_1+a_2\cdot x_2+a_3\cdot x_3\right) \bmod n$

The set of hash functions defined by $a$ above is a universal hash function set.
