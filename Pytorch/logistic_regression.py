"""Logistic Regression
H(x) = P(X=1;W) = 1-P(X=0;W)

weight Update via Gradient Descent
"""

import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim


x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

optimizer = optim.SGD([W, b], lr=1)

epochs = 1000
for epoch in range(epochs + 1):
    # hypothesis = 1 / (1 + torch.exp(-(x_train.matmul(W) + b)))
    hypothesis = torch.sigmoid(x_train.matmul(W) + b)

    # losses = -(y_train * torch.log(hypothesis) + (1 - y_train) * torch.log(1 - hypothesis))
    # cost = losses.mean()
    cost = f.binary_cross_entropy(hypothesis, y_train)

    optimizer.zero_grad() # 0으로 초기화
    cost.backward()       # back propagation
    optimizer.step()

    if epoch % 100 == 0:
        print("Epoch {:4d}/{} Cost: {:.6f}".format(
            epoch, epochs, cost.item()
        ))
