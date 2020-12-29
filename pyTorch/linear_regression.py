# Linear Regression
"""
1. Data definition
- What would be the grade if I study 4 hours?

Training dataset
x : hour , y : points
1 hour -> 2 points
2 hour -> 4 points
3 hour -> 6 points
4 hour -> ? points

2. Hypothesis
- y = Wx + b

3. Compute loss
- Mean Squared Error (MSE)

4. Gradient descent
- SGD
"""
import numpy as np
import torch

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])

W = torch.zeros(1, requires_grad=True) #requires_grad로 학습대상 지정
b = torch.zeros(1, requires_grad=True)

optimizer = torch.optim.SGD([W, b], lr=0.01)

epochs = 1000

for epoch in range(1, epochs + 1):
    hypothesis = x_train * W + b
    cost = torch.mean((hypothesis - y_train) ** 2)
    
    optimizer.zero_grad() # gradient 초기화
    cost.backward() # gradient 계산
    optimizer.step() # 개선