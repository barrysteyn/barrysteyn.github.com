Date: 2013-02-06
Title: Mathematical Nonsense - Logarithm Equality
Tags: Math, Mathematical_Nonsense
Slug: Mathematical_Nonsense_Lemma-For-Logarithm-Equality
Category: Blog
Latex:

It's been many years since I was first taught [logarithms](http://en.wikipedia.org/wiki/Logarithm). So when looking at a proof that hinged on the fact that $a^{log_b n} = n^{log_b a}$, I thought that the proof was wrong. Actually, it was my fault: $a^{log_b n}$ is indeed equal to $n^{log_b a}$, I just forgot.

And so, I thought I would prove this fact. I am going to call it mathematical nonense, and its just short little lemmas that give me pleasure to prove and to reread.

\begin{aligned}
a^{log_b n} &= X & \cr
log_b (a^{log_b n}) &= log_b (X) \cr
log_b n \cdot log_b a&= log_b(X) \cr
log_b a \cdot log_b n&= log_b(X) \cr
log_b n^{log_b a}&= log_b(X) & \cr
n^{log_b a}&= X = a^{log_b n} & \cr
\end{aligned}
