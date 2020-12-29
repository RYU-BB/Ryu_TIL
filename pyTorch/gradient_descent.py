"""Gradient descent

hypothesis(Linear Regression)
H(x) = Wx + b
"""
import torch

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

W = torch.zeros(1)
lr = 0.1

epochs = 10

for epoch in range(1, epochs+1):
    hypothesis = x_train * W
    
    cost = torch.mean((hypothesis - y_train) ** 2)
    gradient = torch.sum((W * x_train - y_train) * x_train)
    
    print("Epoch {:4d}/{} W: {:.3f}, Cost: {:.6f}".format(epoch, epochs, W.item(), cost.item()))
    
    W -= lr * gradient
    
W = torch.zeros(1, requires_grad=True)
optimizer = torch.optim.SGD([W], lr=0.15)

print("\nuse optimize")
for epoch in range(1, epochs+1):
    hypothesis = x_train * W
    
    cost = torch.mean((hypothesis - y_train) ** 2)
    
    print("Epoch {:4d}/{} W: {:.3f}, Cost: {:.6f}".format(epoch, epochs, W.item(), cost.item()))
    
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()