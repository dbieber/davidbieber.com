+++
title = "Weak and Strong Law of Large Numbers"
date = 2021-07-18T00:00:00
tags = ["tech-tips"]
math = true
+++

$X_i$s are i.i.d random variables with finite expected value.

$S_n$ is the sum of first $n$ random variables (the sample mean).<br/>
$\mu$ is the true mean (the population mean).

Both the _Weak Law of Large Numbers_ and the _Strong Law of Large Numbers_ say that sample mean likely converges to the population mean as sample size increases.

The Weak law guarantees _convergence in probability_.<br/>
The Strong law guarantees _almost sure convergence_.

Weak law: $\lim\limits_{n \to \infty} \text{Pr}\left(|S_n - \mu| < \epsilon\right) = 1$<br/>
Strong law: $\text{Pr}\left(\lim\limits_{n \to \infty} S_n = \mu\right) = 1$

Neither occurence of "$=1$" means that any event is guaranteed. There's simply infinitesimal probability that an event does not occur.

The weak law says that for any threshold distance from the true mean $\epsilon$ that you select, as the number of samples increases, the probability that the sample mean is within $\epsilon$ from the true mean approaches one. Even as the number of samples increases there is still the possibility of the sample mean being further than $\epsilon$ from the true mean; that possibility simply approaches being infinitesimal as the number of samples increases.

The strong law similarly doesn't guarantee that the sample mean must ever equal the true mean. It says that with probability 1 (aka "almost surely") the limit of the sample mean equals the true mean.
The reason we call probability 1 "almost surely" rather than "surely" is that there are still valid sequences of samples where the sample mean doesn't approach the true mean; these sample outcomes are simply an infinitesimal fraction of the total sample space.
