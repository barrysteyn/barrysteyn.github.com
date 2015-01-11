Date: 19-12-2012 
Title: Base64 With OpenSSL C API
Slug: Base64-With-OpenSSL-C-API
Author: Barry Steyn
Category: Blog
Tags: Development,OpenSSL
Github: https://gist.github.com/4409525
Latex:

OpenSSL has the ability to perform [Base64](http://en.wikipedia.org/wiki/Base64) encodings and decodings. There seems to be many queries for working examples on how to use this functionality. Unfortunately, the [example](http://www.openssl.org/docs/crypto/BIO_f_base64.html) on the OpenSSL site is quite obtuse, and every other example I have come accross does not work. So here is some [working code](https://gist.github.com/4409525/download). Enjoy!

#Get The Code
You can download this entire gist [here](https://gist.github.com/4409525/download). It consists of the following files:

* [Base64Decode.c](https://gist.github.com/4409525#file-base64decode-c) - the decode function (takes Base64 encoded string as input).
* [Base64Encode.c](https://gist.github.com/4409525#file-base64encode-c) - the encode function (takes a "normal" string as input).
* [Main.c](https://gist.github.com/4409525#file-main-c) - the main c file that demonstrates usage of the functionality in the two files above.
* [Makefile](https://gist.github.com/4409525#file-makefile) - the C makefile. Compilation has been tested on a linux ubuntu distribution, and links with `lcrypto` for [opensll](http://www.openssl.org/) and `lm` for math.

#Base64 Encoding
<script src="https://gist.github.com/4409525.js?file=Base64Encode.c"></script>

Note the following:

* Given a string of length `n`, the resulting Base64 string is length $4 *\lceil \frac{n}{3} \rceil $. This is performed on line 12.
* On line 13, `*buffer` is malloc'd to `encodedSize+1`. The `+1` is because an extra character is needed for the `NULL` character (`'\0'`) at the end of the string.

#Base64 Decoding
<script src="https://gist.github.com/4409525.js?file=Base64Decode.c"></script>

Note the following:

* It is important to set the flag `BIO_FLAGS_BASE64_NO_NL`. If this is not done, the read operation will block until a newline character (`\n`) is encountered.
* The function `calcDecodeLength` will, given a Base64 encoded input string, calculate the length of the decoded string. Base64 encodes a "normal" 8 bit character string by using only 6 bits (hence only $2^6=64$ characters are needed). Therefore every 4 characters of Base64 decodes to three decoded characters, and multiplying the length of the Base64 string by $\frac{3}{4}$ will typically suffice. There are however two exceptions due to padding denoted by the `=` character. For more information, read [decoding base64 with padding](http://en.wikipedia.org/wiki/Base64#Decoding_Base64_with_padding).

#Usage
The above functionality is used like so:
<script src="https://gist.github.com/4409525.js?file=Main.c"></script>

Compile it with this MakeFile:
<script src="https://gist.github.com/4409525.js?file=Makefile"></script>

#Memory Stuff
The memory for `buffer` in both functions is created on the heap using [malloc](http://www.cplusplus.com/reference/cstdlib/malloc/). Therefore, it must be managed. This is a tiny example, and the program ends before any memory leaks become a problem, but in production code, remember to free the heap memory occupied by `buffer` after it has been used. This is done with the [free](http://www.cplusplus.com/reference/cstdlib/free/) command.

#Conclusion
The above functions should perform better error checking if used in production. It also only works for encoding and decoding of a strings (although it is not too difficult to get it to work for files as well). This should give the inquisitive (and frustrated) programmer a base from which to work from.
