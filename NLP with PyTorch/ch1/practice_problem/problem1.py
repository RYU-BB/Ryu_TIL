import torch


problem1 = torch.rand(3, 3)
problem1.unsqueeze(0)

problem2 = problem1.squeeze(0)

problem3 = 3 + torch.rand(5, 3) * (7 - 3)

problem4 = torch.rand(3, 3)
problem4.normal_()

problem5 = torch.Tensor([1, 1, 1, 0, 1])
torch.nonzero(problem5)

problem6 = torch.rand(3, 1)
problem6.expand(3, 4)

a = torch.rand(3, 4, 5)
b = torch.rand(3, 5, 4)
problem7 = torch.bmm(a, b)

a = torch.rand(3, 4, 5)
b = torch.rand(5, 4)
problem8 = torch.bmm(a, b.unsqueeze(0).expand(a.size(0), *b.size()))
