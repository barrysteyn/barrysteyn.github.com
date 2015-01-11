Date: 2012-05-20
Title: The 3 Seminal Events In Cryptography
Slug: The-3-Seminal-Events-In-Cryptography
Author: Barry Steyn
Category: Blog
Tags: cryptography

Cryptography is the art/science of keeping a secret. This need has been present since prerecorded human history, but we have some very famous early examples such as the [Caesar Cipher](http://en.wikipedia.org/wiki/Caesar_cipher). Yet these early examples were very easy to break. It took until the twentieth century for cryptography to be rigorously defined and useful to a wider audience, and it was largely done so in three seminal papers:

1. *Communication Theory of Secret Systems* by [Claude Shannon](http://en.wikipedia.org/wiki/Claude_Shannon)
2. *New Directions In Cryptography* by [Whitfield Diffie](http://en.wikipedia.org/wiki/Whitfield_Diffie) and [Martin Hellman](http://en.wikipedia.org/wiki/Martin_Hellman)
3. *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems* by [Ronald Rivest](http://en.wikipedia.org/wiki/Ron_Rivest), [Adi Shamir](http://en.wikipedia.org/wiki/Adi_Shamir) and [Leanard Adleman](http://en.wikipedia.org/wiki/Leonard_Adleman)

For this explanation, it helps to give a quick definition of the cryptographic process. A message (called the plain text) must be encrypted to cipher text. It is done so via an algorithm that takes two inputs - the *plain text* to be encrypted, and a *secret key*.

#Communication Theory of Secret Systems by Claude Shannon
How does one define security of a cipher? This question had not been rigorously answered until the above paper in 1949 by Claude Shannon was published. Claude Shannon has often been called the father of the digital world. One of the founding fathers of this amazing age that we live in, there is hardly anything that we take for granted in the electronic age that Claude Shannon did not have a hand in designing.

Thank goodness Shannon had some spare time to devote to cryptography. His paper defines a secure cipher as *not letting anyone learn anything about the plain text given just the cipher text*. He thus defines a perfect cipher as the following: Given a cipher text, the probability that it resulted from any plain text is equal. Okay, that does not sound so special, but that is because I dumbed it down a bit. It actually means that when you are given some cipher text, you have absolutely no idea what plain text was used as input to produce the cipher text, seeing as all plain text have the same probability to produce the cipher text, it could have been any plain text - we just don't know!

Unfortunately, Shannon also proved that in order to have this perfect security, one needs a key at least as big as the message space. This makes perfect security impracticable: Given a message that it is a few gigabytes of size, the key to producing a perfect cipher must also be a few gigabytes large! So modern cryptography tries to relax the conditions of perfect security by defining something called *semantic security*. Semantic security says that no efficient algorithm must have the ability to determine what plaintext produced the cipher text. More importantly, by relaxing Shannon's security definition, we are able to use keys that are tiny in comparison. Because it is not perfect by Shannon's definition, an algorithm can be produced that should be able to break the cipher. But as long as we make it so that the effort required is tantamount to waiting until the end of the universe, we are safe.

Semantic security defines our modern cryptographic age. To be sure, if a cipher is semantic secure, it can also suffer from *chosen plaintext attacks* and *chosen ciphertext attacks*, but at least now we have a base metric which we can use to measure how effective our security is. And indeed, modern cryptographic atomics, like AES (advanced encryption standard) is as far as we know, semantically secure. And so we use it all the time.

#New Directions In Cryptography by Whitfield Diffie and Martin Hellman

The next big thing that happened has all to due with secret keys. A cipher such as AES is semantically secure, and so using it should be secure for two parties. But how can two parties agree upon a secret key to use with encryption without letting anyone know? In the Internet age, this problem is even more acute than one may suspect: Given two people that are separated by vast geographical distances and connected by the Internet who wish to communicate securely, how do they agree upon a secret key without anyone else being able to discover this secret key. The Internet is a very insecure medium by fact of anyone being able to connect to it. So agreeing upon a secret key in a secure manner over an insecure medium is not a trivial problem.

Diffie-Hellman to the rescue! Their seminal paper allows us to perform the amazing feat of securely agreeing upon a secret over an insecure medium. I'm going to save it for another post in order to explain how Diffie-Hellman works (it requires some math background), but suffice it to say that Diffie-Hallman makes it possible for secure communication to happen anywhere over any connection.

#A Method for Obtaining Digital Signatures and Public-Key Cryptosystems by Ronald Rivest, Adi Shamir and Leanard Adleman

The last of the seminal papers was a really huge idea. Up until now, people had used the same key to both encrypt and decrypt their messages. One could think about encryption as a door with a lock: The same key used to lock the door is also used to unlock the door. The above paper changed all that!

Commonly known as RSA (taken from the first letter of the surnames of the three inventors), it ushered in the era of *public key encryption*, and allowed cryptography to do more than just keep secrets - it allowed cryptography to also uniquely identify a party thus making digital signatures possible.

Public key cryptography works by having two keys: A public key, and a private key. The names are very descriptive: A public key is kept public and is shared with the world, a private key is kept private and may not be shared with anyone. If one encrypts with one key, then one must use the other key to decrypt. So if two users wish to communicate securely, then one of the users just asks for the other user's public key. The message is then encrypted using the public key, but the user with the private key is the only entity able to decrypt it. So it is useless to anyone else.

Just as interesting is if something is encrypted using the private key. Only the public key can be used to decrypt. This may seem counter-intuitive at first, but think about what problem this solves. If I have your public key, and you give me something encrypted using your private key, then I am able to ensure that you are the person - and not anyone masquerading as you - who encrypted the message. This is because you are the only person with the private key. So your public key will only work with things that are encrypted with your private key, something which only you have access to. And this is the essence of a digital signature.

**Update**: I have written two blog posts explaining [how RSA works](http://doctrina.org/How-RSA-Works-With-Examples.html) and [why RSA works](http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html).
