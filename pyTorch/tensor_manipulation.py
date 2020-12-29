"""
2d tensor(Typical Simple Setting) t = (batch size, dim)
3d tensor(Typical Computer Vision) t = (batch size, width, height)
3d tensor(Typical NLP) t = (batch size, length, dim)
""" 

import numpy as np
import torch

# 1D array with Numpy
t = np.array([0., 1., 2., 3., 4., 5., 6.])
print("1D Arary t:", t)
print("Rank of t: ", t.ndim)
print("Shape of t: ", t.shape)

# 2D array with Numpy
t = np.array([[1., 2., 3.], 
              [4., 5., 6.], 
              [7., 8., 9.], 
              [10., 11., 12.]])
print("\n2D Array t\n", t)
print("Rank of t: ", t.ndim)
print("Shape of t: ", t.shape)

#1D array with pyTorch
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print("\npytorch 1D Arary t\n", t)
print("Rank of t: ", t.ndim)
print("Shape of t: ", t.shape)

#2D array with pyTorch
t = torch.FloatTensor([[1., 2., 3.], 
                       [4., 5., 6.], 
                       [7., 8., 9.], 
                       [10., 11., 12.]])
print("\npytorch 2D array t\n",t)
print("Rank of t: ", t.ndim)
print("Shape of t: ", t.shape)

#smae shape
m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print("\nsame shape add: ",m1 + m2)

# vector + scalar
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([3])
print("\nvector + scsalar: ",m1 + m2)

# 2 x 1 vector + 1x 2 vector
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print("\n2 x 1 vector + 1x 2 vector: ", m1 + m2)

# Multiplication vs Matrix Multiplication
print("Matrix Multiplication")
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print(m1.matmul(m2))
print("Multiplication")
print(m1 * m2)

# Mean
print("1D array mean")
t = torch.FloatTensor([1, 2])
print(t.mean)

# Can't use mean() on integers

print("2D array mean")
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.mean())

# Max and Argmax
t = torch.FloatTensor([[1, 2], [3, 4]])
print("\nmax and Argmax: ", t.max(dim=0))
