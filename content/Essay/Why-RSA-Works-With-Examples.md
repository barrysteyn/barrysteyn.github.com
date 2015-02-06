Date: 2012-09-03
Title: Why RSA Works: Three Fundamental Questions Answered
Tags: cryptography
Slug: Why-RSA-Works-Three-Fundamental-Questions-Answered
Subcategory: Cryptography

[TOC]

This is part two of a series of two blog posts about RSA ([part 1](http://doctrina.org/How-RSA-Works-With-Examples.html) explains *how* RSA works). This post examines *why* RSA works as it does by answering *three* fundamental questions:

1. Why opposite keys must be used.
2. Why RSA is *correct*.
3. Why the inverse of a key is calculated with respect to the [Totient](http://doctrina/How-RSA-Works-With-Examples.html#eulers-totient).

Some parts of this post will be mathematical, but I am going to give as many examples as possible to aid understanding. Before reading this post, it is essential that the background math section of the [previous post](http://doctrina.org/How-RSA-Works-With-Examples.html) is understood.

#Background Mathematics
##Fermat's Little Theorem <a id="flt"></a>
[Pierre de Fermat](http://en.wikipedia.org/wiki/Pierre_de_Fermat) can only be described as an absolute legend! This theorem of his was made sometime in the 17th century. He could not have fathomed how useful it would be to RSA encryption. 

It is actually very simple: For any prime number $p$ and any integer $a$, $a^p \equiv a \bmod p$. In English, this says that an integer $a$ raised to the power of a prime number $p$ will result in a number that when divided by the prime number $p$ produces a remainder that is $a$. **Example**: Let $p=2$ and $a=5$. Then $2^5 = 32 = 2 \bmod 5$.

If we manipulate the theorem slightly by dividing the equation by $a$, we get the form that is most useful to RSA:

\begin{equation}
	\label{bg:flt} a^{p-1} \equiv 1 \bmod p
\end{equation}

Equation $\ref{bg:flt}$ is able to be divided by $a$ (i.e. $a^{-1}$ exists in $\bmod p$) because $a$ is relatively prime to $p$ (i.e. $gcd(a,p) = 1$) due to the definition of $p$ being a prime number. And any two relatively prime integers means the smaller integer has an inverse with respect to the modulus of the larger integer.

**Example**: Lets stick with our previous example:
$$2^{5-1} = 2^4 = 16 = 1 \bmod 5$$

Here is another one: 
$$6^{13-1}= 6^{12} = 2176782336 = 1 \bmod 13$$

#RSA - A brief recap
A brief recap is in order. For RSA to work, we need the following things (these are all explained in more detail in my previous [post](http://doctrina.org/How-RSA-Works-With-Examples.html#RSA)):

1. Two large randomly generated primes, denoted by $p$ and $q$.
2. A *modulus* $n$, calculated by multiplying $p$ and $q$: $n = p \cdot q$.
3. The *totient of* $n$, represented by $\phi(n)$ and calculated like so: $\phi(n) = (p-1)\cdot (q-1)$.
4. The *public exponent* $e$ which is often just chosen to be *65537* (unless it is a factor of the *totient*, in which case the next largest prime number is chosen).

With the above information, the *private* exponent can be calculated (by using the [Extended Euclidean Algorithm](http://en.wikipedia.org/wiki/Extended_euclidean_algorithm)). The private exponent, denoted by $d$ is the inverse of the public exponent with respect to the *totient*. Keys in RSA are the pair consisting of the exponent and the modulus. It is represented like so:

>**Public Key**: $(e,n)$  
>**Private Key**: $(d,n)$

Encryption (denoted by $E$) and decryption (denoted by $D$) are performed by raising a plaintext message (denoted by $m$) to one of the keys, and then dividing by $n$ to obtain the remainder. Cipher text is denoted by $c$. These operations are represented like so:

>**Encryption** (With Public Key): $E(e,m) = m^e \bmod n = c$  
>**Decryption** (With Private Key): $D(d,c) = c^d \bmod n = m$

#RSA - Why It Works

##Why opposite keys must be used
It is sometimes misunderstood that encryption can only happen with the *public key* and decryption with the *private key*. This statement is not true. In RSA, both the *public* and the *private* keys will encrypt a message. If that message is to be decrypted, then the opposite key that was used to encrypt it must be used to decrypt it. Underlying this statement is this fundamental equation:

\begin{equation}
e\cdot d = 1 \bmod \phi(n)
\end{equation}

That is, the public key $e$ is the inverse of the private key $d$ with respect to $\phi(n)$, so multiplying them together will produce $1 \bmod \phi(n)$. Multiplication is commutative, which means it can happen in any order. Both $e\cdot d$ and $d\cdot e$ will produce the same $1 \bmod \phi(n)$. Why is this important? I will give a correct (and more formal) proof [below](http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html#correctness), but for the sake of what follows, consider these arguments: 

+ If one raises a message to one of the keys (lets choose the private key $d$), then the cipher $c$ will be $ m^d \bmod n$. 
+ In order to get the original message back, note that raising a number to $1$ will result in the original number. 
+ So to get $m$, we raise $c$ to $e$, which gets us $c^e = m^{d\cdot e} = m^1 = m$, our original message (again, this is not entirely correct, but it will suffice in understanding this concept).

When multiplying exponents, the commutative aspect of multiplication applies: $x^{a\cdot b} = x^{b\cdot a}$. For example, $2^{3\cdot 2} = 2^{2\cdot 3} = 2^6 = 64$. With respect to the public and private keys, when carrying out a RSA operation (either encryption or decryption), all that really happens is that the message is raised to an exponent value of the key. Therefore if one of the key exponents is used to encrypt a message, it necessary to use the other key in order to obtain the *exponent value of $1$* that is necessary to get our original message.

Mathematically, the following must be shown:

$$D(d,E(e,m)) = m = D(e,E(d,m))$$

That is, decrypting a message with the private key that was encrypted with the public key is the same as decrypting a message with the public key that was encrypted with the private key. This can be easily shown:

$$
D(d,E(e,m)) = D(d,m^e \bmod n) = \textbf{m}^{\textbf{e}\cdot \textbf{d}} \bmod n = \textbf{m}^{\textbf{d} \cdot \textbf{e}} \bmod n = D(e,m^d\bmod n) = D(e,E(d,m))
$$

I have bold-ed the crucial part of the math above, namely the comutative property of the exponent. The math above can be stated in English like so:
> $D(d,E(e,m)) = m$ : decrypting using the private key will only work on a message encrypted using the public key.  
> $D(e,E(d,m)) = m$ : decrypting using the public key will only work on a message encrypted using the private key.

This may seem simple and obvious when reading, but it is the reason behind RSA's two atomic uses:

1. **Encryption**: The public key, which anyone can gain access to, can be used to encrypt information that only the recipient with the private key can decrypt.
2. **Identity**: If one needs to prove that a message originated from someone, then if the message can be decrypted using the person's public key, it must originate from that person because that person is the only one who has the private key.

It is the second use in my opinion that makes RSA so useful. Things like *electronic voting*, *digital signatures*, *mix nets* etc become possible because of this. This is not to play down the importance of the first use, which is critical for things like SSL.

##Why RSA Satisfies The Correctness Equation <a id="correctness"></a>
The correctness equation (also called the consistency equation) simply states that ciphertext $c$ originating from a message $m$ must equal to $m$ when decrypted. In other words, decrypting the ciphertext must produce the original message: $D(d,E(e,m)) = m$. It is not only fundamental to RSA, but to any encryption atomic. In fact, I would say that the first thing a person would have to prove if they invent a new cryptographic algorithm is that it conforms to the correctness equation.

**Helpful hint**: I would advise the reader who is serious about this topic to get a pen and paper and work through the below math as I present it. It is not difficult math, but it can get quite confusing if you are just reading this. I also think that this topic can be explained more succinctly than I have presented it, but for the sake of clarity, I have gone into great detail.

Recall that encrypting a message $m$ with a key exponent $e$ will result in cipher text $c$ that is $m^e \bmod n$. When raising that cipher text to the opposite key exponent $d$, the original message $m$ must result. In other words, $m = c^d = m^{e \cdot d}$. Therefore raising $m$ to $e\cdot d$ must result in $m$. If this can be proven, we have then proved the correctness property.

From the section above, the private key is the inverse of the public key with respect to $\phi(n)$, multiplying them together is equivalent to $1 \bmod \phi(n)$. In my [previous post](http://doctrina/How-RSA-Works-With-Examples.html#integer-remainder-after-dividing), I showed that this means that $e\cdot d = k\cdot \phi(n) + 1, k \in \mathbb{Z}$.

$D(d,E(e,m)) = m^{e\cdot d} \bmod n = m^{k\cdot \phi(n) + 1} \bmod n$. Recall that $p-1$ divides $\phi(n)$ because $\phi(n) = (p-1)\cdot (q-1)$, so $m^{\phi(n)\cdot k + 1} \bmod n = m^{(p-1)\cdot (q-1)\cdot k + 1} \bmod n$. Lets concentrate on proving the equation for $p$:

$m^{(p-1)\cdot (q-1)\cdot k + 1} \bmod n = \left( m^{p-1} \right)^{(q-1)\cdot k}\cdot m \bmod n$. From [Fermat's Little Theorem](http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html#flt), since $p$ is prime, $m^{p-1} = 1 \bmod p$. Therefore $\left( m^{p-1} \right)^{(q-1)\cdot k}\cdot m = (1 \bmod p)^{(q-1)\cdot k}\cdot m \bmod n$. But because $p$ divides $n$, we can write the previous equation like so: $\left( m^{p-1} \right)^{(q-1)\cdot k}\cdot m = 1\cdot m \bmod p$. Thus the following equation holds:

\begin{equation}
\label{almost} m^{e\cdot d}\bmod n \equiv m \bmod p
\end{equation}

The above equation is almost there, but there is one glaring problem: We have proved equality to $m \bmod p$, not $m \bmod n$. To prove that is indeed equal to $1 \bmod n$, note that for equation $\ref{almost}$ above, we can substitute $p$ for $q$ so that $m^{e\cdot d}\bmod n \equiv m \bmod q$. This is easily done, as $q$ is also prime, just like $p$ and hence it will obey [Fermat's Little Theorem](http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html#flt). So we now have the following two equations:

$$
m^{e\cdot d}\bmod n \equiv m \bmod p
$$
$$
m^{e\cdot d}\bmod n \equiv m \bmod q
$$

Since $n = p\cdot q$, if an equation is equal to both $m \bmod p$ and $m \bmod q$, then it is also equal to $m \bmod p\cdot q$ which is $m \bmod n$. And thus:

\begin{equation}
\label{wearethere} m^{e\cdot d}\bmod n \equiv m \bmod n
\end{equation}

And this proves the correctness of RSA:

\begin{equation}
D(d,E(e,m)) = m
\end{equation}


##Why RSA uses inverses with respect to the Totient <a id="wruiwrtt"></a>
The private key $d$ is the inverse of the public key $e$ with respect to $\phi(n)$. But why choose $\phi(n)$ to calculate the private key? It was proven above that using $\phi(n)$ gives an algorithm that will satisfy correctness. But this is not the only reason why $\phi(n)$ is used! Before answering this question, lets state what is *public* and what is *secret* in RSA:

<center>
<table style="border-style: solid; border-width:1px; border-color: #000000;">
	<tr>
		<td><b>Public</b></td>
		<td><b>Secret</b></td>
	</tr>
	<tr>
		<td><ul>
			<li> $n$ - the modulus</li>
			<li> $e$ - the public exponent</li>
			<li> $c$ - the cipher text</li>	
		</ul></td>
		<td><ul>
			<li> $p$ - the prime factor of $n$</li>
			<li> $q$ - the other prime factor of $n$</li>
			<li> $\phi(n)$ - the totient of $n$</li>
			<li> $d$ - the private exponent
		</ul></td>
	</tr>
</table>
</center>

RSA's security lies in the fact that it is difficult to deduce what is secret given what is public. When describing RSA's security, the word *difficult* is used a lot. The reason being that deducing what is secret from what is public cannot be proven to be impossible! This is because the security relies upon a problem that is considered *hard*: Given $n$, find its prime factors, $p$ and $q$. This cannot be proven to be impossibly difficult and therefore it may seem scary and odd that we place so much vital information in the trust of an algorithm that cannot be proven secure. Solace is taken in the fact that very clever people in the present and the past have all tried and failed to quickly factorise large numbers into their prime constituents. Also, there is some evidence to believe that whilst we can never prove security, it is in fact [secure](http://en.wikipedia.org/wiki/Integer_factorization#Difficulty_and_complexity). But if one can find the prime factors of $n$, then it is easy to calculate $\phi(n)$ which is $(p-1)\cdot (q-1)$. With $\phi(n)$ at your disposal, calculating $d$ given $e$ is simple (use the [Extended Euclidean Algorithm](http://en.wikipedia.org/wiki/Extended_euclidean_algorithm) to do this).

So we use $\phi(n)$ to calculate the inverse because it is hard for anyone to determine it given the public information, and therefore calculate the private key.

#Conclusion
RSA works! There are many more interesting things to discuss about RSA, and books can be (and [have been](http://www.amazon.com/The-Mathematics-Ciphers-Number-Cryptography/dp/1568810822/ref=sr_1_3?ie=UTF8&qid=1346693118&sr=8-3&keywords=RSA)) written about this subject. But hopefully with my [previous post](http://doctrina.org/How-RSA-Works-With-Examples.html) and this post combined, the reader will have a solid understanding of this wonderful cryptographic algorithm.