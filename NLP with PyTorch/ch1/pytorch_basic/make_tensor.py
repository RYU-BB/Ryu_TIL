import torch


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