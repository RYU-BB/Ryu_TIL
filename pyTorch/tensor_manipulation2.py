import numpy as np
import torch

# View (Reshape)
t = np.array([[[0, 1, 2],
              [3, 4, 5]],
             
             [[6, 7, 8],
              [9, 10, 11]]])
ft = torch.FloatTensor(t)
print("ft shape: ",ft.shape)
print("view [-1,3]:\n ", ft.view([-1, 3]))
print("shape: ", ft.view([-1, 3]).shape)

print("\nview [-1, 1, 3]:\n", ft.view([-1, 1, 3]))
print("shape: ", ft.view([-1, 1, 3]).shape)

# squeeze (쥐어짜는 것)
ft = torch.FloatTensor([[0], [1], [2]])
print()
print(ft)
print(ft.shape)
print("squeeze: ", ft.squeeze())
print("squeeze shape: ", ft.squeeze().shape)

# unsqueeze
ft = torch.Tensor([0, 1, 2])
print(ft.shape)
print("unsqueeze dim = 0: ", ft.unsqueeze(0))
print("shape: ", ft.unsqueeze(0).shape)

print("view [1,-1]: ", ft.view(1, -1))
print("shape: ", ft.view(1, -1).shape)

print("unsqueeze(1): ", ft.unsqueeze(1))
print("shape: ", ft.unsqueeze(1).shape)

print("unsqueeze(-1): ", ft.unsqueeze(-1))
print("shape: ", ft.unsqueeze(-1).shape)

# Type Casting
lt = torch.LongTensor([1, 2, 3, 4])
print("\ntype casting")
print(lt)
print(lt.float())

bt = torch.ByteTensor([True, False, False, True])
print(bt.long())
print(bt.float())

# Concatenate
print()
print("concatenate")
x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.FloatTensor([[5, 6], [7, 8]])
print(torch.cat([x, y], dim=0))
print(torch.cat([x, y], dim=1))

# Stacking
print()
print("Stacking")
x = torch.FloatTensor([1, 4])
y = torch.FloatTensor([2, 5])
z = torch.FloatTensor([3, 6])
print(torch.stack([x, y, z]))
print(torch.stack([x, y, z], dim=1))
print(torch.cat([x.unsqueeze(0), y.unsqueeze(0), z.unsqueeze(0)], dim=0))

# Ones and zeros
# 같은 device에서 연산을 위해 like 사용
print()
print("Ones and zeros")
x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
print(x)
print(torch.ones_like(x))
print(torch.zeros_like(x))

# In-place Operation
x = torch.FloatTensor([[1, 2], [3, 4]])
print()
print("In-Place Operation")
print(x.mul(2.))
print(x)
print(x.mul_(2.))
print(x)

