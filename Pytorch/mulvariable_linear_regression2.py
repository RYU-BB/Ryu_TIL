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
import torch.nn as nn
import torch.nn.functional as f

x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 80],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

model = nn.Linear(3, 1)

optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

epochs = 2000
for epoch in range(epochs + 1):

    prediction = model(x_train)
    cost = f.mse_loss(prediction, y_train)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print("Epoch {:4d}/{} Cost: {:.6f}".format(
            epoch, epochs, cost.item()
        ))
