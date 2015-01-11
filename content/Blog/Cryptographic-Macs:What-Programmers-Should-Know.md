Date: 2013-02-17
Title: Cryptographic Hash VS MAC: What You Need To Know
Tags: cryptography
Slug: Cryptographic-Hash-Vs-MAC:What-You-Need-To-Know
Category: Blog
Latex:

A MAC ([message authentication code](http://en.wikipedia.org/wiki/Message_authentication_code)) is an important part of the cryptographic arsenal. It ensures message integrity and eliminates a very dangerous type of attack - *active attacks* (whereby an atacker changes the message payload tricking both communicating parties).

A MAC is often confused with a cryptograhic hash (i.e. SHA256), and while they are similar, using a crytographic hash instead of a MAC will have devastatingly insecure consequences. I think it was an unfortunate choice of words to call it a *cryptographic hash*, because as I will show , a cryptographic hash is not even designed to be secure. 

This article aims to set things right. It will explain the following:

 * What a cryptographic hash is.
 * Why a cryptographic hash is insecure, and when it should be used.
 * What a MAC is.

#Cryptographic Hash
A hash function maps an input in a large space to an output in a small space. Known as compression, all hash functions exhibit this property. A hash function's classic use is in the creation of a hash table, where it is vital that hash outputs are indepedendent of its inputs (because inputs who are related may be assigned to the same hash bucket). 

A cryptographic hash function is hash function with four properties:

 1. **Compression**
 2. **Pre-Image Resistance**
 3. **Weak Collision Resistance**
 4. **String Collision Resistance**

The last two properties are known collectively as *collision resistance*.

###Compression
A compression function produces an output that is vastly smaller than its input (hence the name compression). More formally, the size of the domain (i.e. input) is much larger than the size of the range (i.e. output). For those math type people out there, it is expressed like so:

<center>$H: M \rightarrow x, M \in \\{0,1\\}^n, x \in \\{0,1\\}^l$ where $l \ll n$</center>

###Pre-Image Resistance
Pre-image resistance means that given the result of a hash, it is hard to determine the message that produced that hash. Assuming the result of hashing a message $M$ is $x$, then given only $x$, it is hard to recover $M$.

###Weak Collision Resistance
Weak collision resistance means that given the result of a hash, it is hard to find *another* message that hashes to that same result. Therefore given $x \leftarrow H(M_0)$, it is hard to find $M_1 \neq M_0$ such that $x \leftarrow H(M_1)$. This is in some way similar to pre-image resistance, and weak collision resistance implies a form of pre-image resistance. But they are not the same thing.

###Strong Collision Resistance
Strong collision resistance means that is hard to find any two messages that hash to the same value. That is, it is hard to find $M_0$ and $M_1$ such that $H(M_0) = H(M_1)$. 

##Don't Get Confused!
If a weak collision is found, then one has also automatically found a strong collision (and vice-versa). So its easy to get confused and think they are the same thing, but they are not. A weak collision implies a hash collision for a message that has already been chosen. A strong collision implies a hash collision between any two messages. It is more difficult to achieve strong collision resistance due to the [Birthday Paradox](http://en.wikipedia.org/wiki/Birthday_paradox), hence the names strong and weak.

# Message Integrity
Message integrity ensures a message is not altered during transmission. In short, the same message that was sent is the same that was received. For networking, various protocols have been built to ensure message integrity, like the ever popular and ubiquitous TCP protocol that ensures the message that was sent is the message that was received by using various mechanism including [cyclic redundancy checking](http://en.wikipedia.org/wiki/Cyclic_redundancy_check) (CRC). CRC works well against message integrity being compromised by a network error, but it cannot defend against something more sinister: A hacker who is determined to alter the message payload during transmission (i.e. an active attack).

Message integrity is defended against an active attack by transmitting the message along with what is known as a message tag. The receiving party computes their own tag on the received message, and if it matches the transmitted tag, message integrity is assured. 

## Tag Security: Existential Forgery
The mechanism used to build a tag needs to be secure. There are many rigorous security definitions for a tag, but an informal security definition would be to make it impossible for an attacker (i.e. anyone besides the person who created the original valid message tag pair) to produce a new message with a valid tag. Being able to produce a new message with a valid tag is called an *existential forgery*, and any tag worth its weight must defend against existential forgery.

#A Cryptrographic Hash Is Not Secure
A crypgtographic hash (like the [SHA-2](http://en.wikipedia.org/wiki/Sha256) family of hashes - e.g. SHA256) is susceptible to an existential forgery. To see this, one needs to have knowledge about how a cryptographic hash is produced. I will therefore give a very brief overview of this process, but I encourage the interested reader to read up more about this topic, I am really only skimming the surface.

##Merkle–Damgård And Davies-Meyer Construction
A block cipher is an encryption mechanism that takes a fixed input of size n bytes, and produces an encrypted output also of size n bytes. There are many block ciphers, and the field has been studied intensely ([AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) is an example). Block ciphers exhibit many of the properties of a crytographic hash, therefore it woulb be nice if a block cipher could be used to construct a cryptographic hash. And it turns out that it can: Any *secure* block cipher can be quickly altered (normally by a method called [Davies-Meyer](http://en.wikipedia.org/wiki/Davies-Meyer#Davies.E2.80.93Meyer)) to have all the properties of a cryptographic hash function except *compression*. Block ciphers need two inputs which are kept secret: A *key* and a *message*. Therefore a cryptographic hash function made from a block cipher also needs two inputs, but unlike a block cipher, neither input is kept secret (read up more on [Davies-Meyer](http://en.wikipedia.org/wiki/Davies-Meyer#Davies.E2.80.93Meyer) to understand these inputs). So how does one get the compression property? It is done using a construction called *Merkle–Damgård*.

The Merkle–Damgård construction takes as input a message of arbitrary length and produces a cryptographic hash of fixed output. It does this by breaking the message up into blocks, then feeding the blocks iteratively into a smaller cryptographic hash function (such as the one discussed in the above paragraph). The output of each function is fed as one of the inputs into the next function. The very first function just has a non-random set initialisation vector (IV) set as one of the inputs.

The image below demonstrates the Merkle–Damgård construction. In this image, **h** is the cryptographic hash created from the block cipher, and $H_n$ is the resulting outputs of each stage. Note how the output of one function is chained to one of the inputs of the other.

<center><img style="margin-left:4px; padding: 4px; background-color: #fff; border: 1px solid #ccc; border: 1px solid rgba(0, 0, 0, 0.2); -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);"src ="http://doctrina.org/static/images/merkle-damgard.png"></img></center>

##Merkle–Damgård Is Not Secure
All our popular cryptographic hash functions are constructed using Merkle–Damgård, but it is very easy to mount an existential forgery attack on anything constructed using the Merkle–Damgård. This is because cryptographic hash functions created with Merkle–Damgård are not designed to be protected from existential forgery (more about this a little later). To see how an existential forgery can happen, study the Merkle–Damgård construction picture. An existential forgery can happen by doing the following:

 1. Obtain a valid message tag pair, say $(M, t_0)$.
 2. Create a new block called $b$.
 3. Now, using a cryptographic hash function (like a Davies-Meyer construction), feed it both $t_0$ and $b$ as inputs, and record the output as $t_1$.
 4. The pair $(M||b, t_1)$ is a valid message tag pair ($M||b$ means $M$ concatenated with $b$).

And so we can very easily make an existential forgery attack for any cryptographic hash function. **NOTE**: For any cryptographer who reads this, I have purposefully ignored padding in Merkle–Damgård (so in reality, the valid message tag pair should be $(M||pad||b, t_1)$).

##The Purpose Of Cryptographic Hashes
A Cryptographic hash's purpose is not to provide message integrity. As will be shown shortly, one needs to have a secret in order to attain message integrity. A cryptographic hash is just a compression function with the extra properties as defined above. This is a very unfortunate choice of name, because most people think that anything with the name crypto means it is secure. In this case, it is not! I think it was named *cryptographic hash* because the crypto guys made the machinery in order to make it possible.

So if it is not secure, does it have any use? Yes, it has tonnes of uses. Just not for message integrity. Here are three uses:

 1. A function to assign inputs to buckets of a hash table. If I have to guess (and this is just a guess), I would say that this is why cryptographic hash functions were invented in the first place - as hash table functions (hence the name *hash*). A cryptographic hash function is in many ways the perfect hash function, as it exhibits secure psuedo-randomness and therefore it is very difficult to determine a pathalogical input data-set for the hash table. Unfortunately, it is quite slow compared to what is needed of hash table functions.
 2. Integrity from a **trusted source** - note, the source must be trusted. For example, you download a file from a website you **trust**. This trusted website has a SHA crytographic hash signature. You calculate your own hash on the file you have just downloaded, and then compare. If they match (again, it is so important that you trust the web site), then you know your code has not been altered.
 3. A means to discover changes in files. Due to collision resistance, if a file changes, its hash will also change (with high probability). This is used to detect changes in such applications as [git](http://en.wikipedia.org/wiki/Git_%28software%29) (and others, I am sure).

#Secure Cryptographic Hash
How does one achieve message integrtity? The answer: A **secure** cryptogrphic hash. This is an example of a [MAC](http://en.wikipedia.org/wiki/Message_authentication_code) and since MAC sounds so different to cryptographic hash, cryptograhers don't get confused (A MAC is more general than a secure cryptographic hash, but a secure cryptographic hash is definitely an example of a MAC). 

A secure cryptogrpahic hash is a cryptographic hash that also involves a secret, and this secret is used to *"lock"* the final tag value in place. Remember when describing the function used in Merkle–Damgård (normally created with Davies-Meyer construction), there is no secret involved. And this is achilles heel for Merkle–Damgård with respect to existential forgery.

Merkle–Damgård is adapted to use secret keys resulting in [HMAC](http://en.wikipedia.org/wiki/Hmac) (which short for hashed based message authenticating code). An attacker would need to know the value of the secret key in order to mount an existential forgery attack. However, the key is a secret shared only between the two communicating parties (there is a whole class of study that is devoted to sharing a key securely between two parties - the interested reader can read about [Diffie-Hellman](http://en.wikipedia.org/wiki/Diffie_hellman)). This makes an existential forgery attack impossible.

#Conclusion
A cryptographic hash is not secure! In order for any hash to be secure, there needs to be a secret known only to the sender and the recipient. This secret is used as a key to lock the hash compression function in place.

So your cryptographic hash is not secure and cannot be used for message integrity without a shared secret!
