+++
title = "Deep Variational Information Bottleneck"
date = 2020-07-21T00:00:00
math = true
+++

You can read the 2017 paper "Deep Variational Information Bottleneck" [on Arxiv here](https://arxiv.org/pdf/1612.00410.pdf), and its reviews are visible [on OpenReview here](https://openreview.net/forum?id=HyxQzBceg). The authors are my coworkers: Alex Alemi, Ian Fischer, Joshua Dillon, and Kevin Murphy.

I've taken notes on the paper, and will use this snippet to present them.

## Notation

We consider the problem of supervised learning for classification with the following notation:
- $X$: An example input.
- $Z$: The output of an intermediate layer of a neural network.
    - We view this as a stochastic encoding of $X$.
    - It is the output of a parametric encoder $p(\textbf{z} | \textbf{x}; \theta)$
    - $\theta$ are the parameters of the neural network used to encode $X$ that we wish to learn.
- $Y$: The example's target class.

## Goal

The approach of the paper aims first and foremost to learn an encoding $Z$ of $X$ that is maximally informative about $Y$.
This is measured via mutual information between $Z$ and $Y$: $I(Z, Y; \theta)$.

$$I(Z, Y; \theta) = \int dx~dy~p(z, y|\theta) \log \frac{p(z, y)}{p(z)p(y)}$$

It's not enough to maximize $I(Z, Y; \theta)$ though; this can be done by simply letting $Z = X$, which isn't useful.

So, we also want to limit $I(Z, X)$. We do this by enforcing an information constraint: $I(X, Z) < I_c$.

Our goal is to maximize $I(Z, Y; \theta)$ subject to $I(X, Z) < I_c$.

Rewriting this using Lagrange multiplier $\beta$ brings us to the information bottleneck (IB) objective, which we write as follows:

$$R_{IB}(\theta) = I(Z,Y) - \beta I(Z, X).$$

The goal of the paper is to maximize $R_{IB}$.

## Intuition Behind Goal

Why maximize $I(Z, Y)$? This is what allows the model to make correct predictions.

Why not just maximize $I(Z, Y)$? Letting $Z = X$ fully maximizes $I(Z, Y)$, but isn't helpful because the representation of $Z$ is what you started with, so its hard to make good classifications.

Why minimize $\beta I(Z, X)$? We want a representation $Z$ that is maximally compressive of the input $X$.

That's the intuition given in the paper for why we seek to minimize $\beta I(Z, X)$, but it isn't clear the degree to which compression is useful. Yes, a compressive representation of $X$ can lead to better generalization, but it's a trade off. Greater compression may mean lower $I(Z, Y)$ and hence lower potential accuracy. Balancing this trade off (choosing an appropriate $\beta$) will be important.

## Why is it difficult?

Mutual information is in general intractable. So we can't directly optimize the object $R_{IB}(\theta)$ as stated in the goal. Instead, the paper takes the following approach to get around mutual information's intractability.

## The Approach

1. Use variational inference to construct a lower bound on the IB objective.

2. Use the "reparameterization trick" and Monte Carlo sampling to get unbiased estimate of gradient.

3. Parameterize our distributions with neural networks, and optimize with SGD.

We'll go into more detail in just a minute.

## Benefits

This approach provides some robustness to overfitting because model ignores as much of $X$ as possible.

It also provides some robustness to adversarial examples because the model maps $X$ to a distribution over $Z$s rather than a single $Z$, so its harder for a single unusual value to influence a final class prediction.

## Execution

### Part 1: Variational Inference

You can follow the math in the paper (Section 3), but the first main result is to define

$$L = \int dx~dy~dz~ p(x) p(y|x) p(z|x) \log q(y|z) - \beta \int dx~dz~ p(x) p(z|x) \log \frac{p(z|x)}{r(z)}$$

and show that 
$$R_{IB}(\theta) = I(Z,Y) - \beta I(Z, X) \ge L.$$

To achieve this, we've introduced $q(y|z)$ as an approximation of $p(y|z)$, and $r(z)$ as an approximation of $p(z)$.

$L$ serves as a lower bound for the objective we care about. $p$, $q$, and $r$ are all parameterized by $\theta$.

We can approximate $L$ as

$$L \approx \frac{1}{N}\sum_{n=1}^N \left[\int dz~ p(z|x_n) \log q(y_n|z) - \beta~ p(z|x_n) \log \frac{p(z|x_n)}{r(z)} \right].$$

### Part 2: Reparameterization trick

Suppose $p(z|x)$ is $N(z|f_e^\mu(x), f_e^\Sigma(x))$, with $f_e$ a neural network that outputs the mean and covariance matrix for the Gaussian.

Then the "reparameterization trick" is to write $p(z|x)dz = p(\epsilon)d\epsilon$, where $z = f(x, \epsilon)$ is a deterministic function and $\epsilon$ is a Gaussian random variable. Using this, we can rewrite $L$ as follows.

$$J_{IB} = \frac{1}{N} \sum\limits_{n=1}^N E_{\epsilon \sim p(\epsilon)} \left[-\log q(y_n|f(x_n,\epsilon))\right] + \beta KL[p(Z|x_n), r(Z)]$$

As long as $q$ is differentiable and $KL[p(Z|x_n), r(Z)]$ is tractable, this is an objective we can optimize with e.g. gradient descent.


## Implementation

A concise demo implementation is available on GitHub at https://github.com/alexalemi/vib_demo/blob/master/MNISTVIB.ipynb.

I've describe here the correspondence between the notation used in the source code and the notation used in the paper.
Terms from the paper are in $\LaTeX$, and terms from the source code are in `code blocks`.

- `class_loss`: $-\log q(y_n | f(x_n, \epsilon))$ (comes from the $I(Z, Y)$ term)
  - Recall $z = f(x, \epsilon)$
  - $q$ is `decoder` with softmax applied, and $q(y | f(x_n, \epsilon))$ is softmax(`logits`)
  - `class_loss = tf.losses.softmax_cross_entropy(
logits=logits, onehot_labels=one_hot_labels) / math.log(2)` is $-\log q(y_n | f(x_n, \epsilon))$
    - $f$ is `encoder`, and $f(x, \cdot)$ is `encoding`
- `prior` is $r(z)$ (which approximates $p(z)$).
