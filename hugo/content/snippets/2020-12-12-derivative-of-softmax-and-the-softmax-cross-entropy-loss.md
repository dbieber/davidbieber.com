+++
title = "Derivative of Softmax and the Softmax Cross Entropy Loss"
date = 2020-12-12T00:00:00

+++

Write $$y_i = \text{softmax}(\textbf{x})_i = \frac{e^{x_i}}{\sum e^{x_d}}$$.

That is, $$\textbf{y}$$ is the softmax of $$\textbf{x}$$. Softmax computes a normalized exponential of its input vector.

Next write $$L = -\sum t_i \ln(y_i)$$. This is the softmax cross entropy loss. $$t_i$$ is a 0/1 target representing whether the correct class is class $$i$$. We will compute the derivative of $$L$$ with respect to the inputs to the softmax function $$\textbf{x}$$.

We have $$\frac{dL}{dx_j} = -\sum t_i \frac{1}{y_i} \frac{dy_i}{d{x_j}}$$

We compute $$\frac{dy_i}{dx_j}$$ using the quotient rule.

If $$i = j$$, this gives:

$$\frac{dy_i}{dx_j} = \frac{\sum e^{x_d} \cdot e^{x_i} - e^{x_i} \cdot e^{x_i}}{(\sum e^{x_d})^2}$$

$$\frac{dy_i}{dx_j} = \frac{e^{x_i}}{\sum e^{x_d}} \cdot \left(\frac{\sum e^{x_d} - e^{x_i}}{\sum e^{x_d}}\right)$$

$$\frac{dy_i}{dx_j} = y_i \cdot (1 - y_i)$$

If $$i \ne j$$, this gives:

$$\frac{dy_i}{dx_j} = \frac{\sum e^{x_d} \cdot 0 - e^{x_i} \cdot e^{x_j}}{(\sum e^{x_d})^2}$$

$$\frac{dy_i}{dx_j} = -\frac{e^{x_i}}{\sum e^{x_d}} \cdot \frac{e^{x_j}}{\sum e^{x_d}} $$

$$\frac{dy_i}{dx_j} = -y_i y_j$$

Together these equations give us the derivative of the softmax function:

$$\frac{dy_i}{dx_j} = \begin{cases} y_i \cdot (1 - y_i) & i=j \\ -y_i y_j & i \ne j \end{cases}$$

Using this result, we can finish computing the derivative of $$L$$. This gives:

$$\frac{dL}{dx_j} = -\sum t_i \frac{1}{y_i} \frac{dy_i}{d{x_j}} = \sum\limits_i \begin{cases} t_i (y_i - 1) & i=j \\ t_i y_j & i \ne j \end{cases}$$

Since exactly one of the $$t_i$$s is 1 and the rest are zeros this further simplifies to:

$$\frac{dL}{dx_j} = y_j - t_j$$

We have computed the derivative of the softmax cross-entropy loss $$L$$ with respect to the inputs to the softmax function.

This page is an experiment in publishing directly from Roam Research. It is incomplete, and the formatting is probably all wonky. Bear with me while I get this sorted.
