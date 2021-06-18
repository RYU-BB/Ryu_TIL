import torch
import numpy as np


def describe(x):
    print("타입: {}".format(x.type()))
    print("크기: {}".format(x.shape))
    print("값: {}".format(x))


describe(torch.zeros(2, 3))
x = torch.ones(2, 3)
describe(x)
x.fill_(5)
describe(x)

x = torch.Tensor([[1, 2, 3],
                  [4, 5, 6]])
describe(x)

x = torch.Tensor([[1, 2, 3],
                  [4, 5, 6]])
describe(x)

npy = np.random.rand(2, 3)
describe(torch.from_numpy(npy))

x = torch.FloatTensor([[1, 2, 3],
                       [4, 5, 6]])

x = x.long()

x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]], dtype=torch.int64)

x = x.float()