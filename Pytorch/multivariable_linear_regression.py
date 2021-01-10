"""Multivariable Linear regression

Simple Linear Regression
H(x) = W * x + b

Multivariable Linear regression
H(x) = W * x + b (multi input)
-> w1 * x1 + w2 * x2 + w3 * x3 + b
-----Data-----
x1 = Quiz 1 score, x2 = Quiz 2 score, x3 = Quiz 3 score
y = Final score

-----goal-----
prediction of y value according to x value based on data
"""

import torch

x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 80],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

W = torch.zeros((3, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

optimizer = torch.optim.SGD([W, b], lr=1e-5)

epochs = 20
for epoch in range(epochs + 1):
    hypothesis = x_train.matmul(W) + b
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    print("Epoch {:4d}/{} hypothesis: {} Cost: {:.6f}".format(
        epoch, epochs, hypothesis.squeeze().detach(), cost.item()
    ))
