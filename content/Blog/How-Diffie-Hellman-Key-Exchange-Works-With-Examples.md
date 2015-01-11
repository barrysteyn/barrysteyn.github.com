Date: 2012-05-26
Title: How Diffie Hellman Key Exchange Works With Examples
Tags: cryptography
Slug: How-Diffie-Hellman-Key-Exchange-Works-With-Examples
Category: Blog
Latex:
Status: draft

In order to attain secure cryptographic communication between two parties, a shared secret key is needed. The shared secret key will most commonly be used to encrypt/decrypt a block cipher (like [AES]()). Most commonly, communication happens over the Internet, which is a very insecure medium. The Internet is combination of public and private equipment that neither of the two communicating parties control. So how can two parties agree upon a unique session key over an insecure medium and guarantee that an evesdropper will not be able to learn the key. The answer: By using *Diffie-Hellman key exchange*.

# The Diffie-Hellman Key Exchange Protocol

##Pick Two Large Prime Numbers Numbers
The Diffie-Hellman key exchange protocol is quite simple. It starts with one of the communicating parties (it does not matter who) picking two numbers. There are only two requirements for these numbers:

1. They must be prime.
2. They must be very large.

The first number that is needed is a very large random prime number, normally ??? ??? digits, which translates into ???? ???? bits. How does one pick such a large prime number in a relatively short time? The answer: a very large number is chosen at random and then tested for primality. If it passes the test, it is prime. If not, 1 is added onto the large number which is then tested for primality again. This procedure carries on until a large prime number is found. The test for primality is a *probablistic* test called the [Rabin-Miller primality tester]() which I have described in a [previous post explaining RSA](). I quote from that post:

 >> [Given to the Rabin-Miller probabilistic tester] a very large number, it is able to quickly determine with a high probability if its input is prime.  But there is a catch (and readers may have spotted the catch in the last sentence): The Rabin-Miller test is a probability test, not a definite test. Given the fact that [Diffie-Hellman] absolutely relies upon generating large prime numbers, why would anyone want to use a probabilistic test? The answer: With Rabin-Miller, we make the result as accurate as we want. In other words, Rabin-Miller is setup with parameters that produces a result that determines if a number is prime with a probability of our choosing. Normally, the test is performed by iterating $64$ times and produces a result on a number that has a $\frac{1}{2^{128}}$ chance of not being prime. The probability of a number passing the Rabin-Miller test and not being prime is so low, that it is okay to use it with RSA.  In fact, $\frac{1}{2^{128}}$ is such a small number that I would suspect that nobody would ever get a false positive.

The large prime number chosen is denoted by $G$. Another prime number 
