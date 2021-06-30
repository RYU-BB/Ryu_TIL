import torch


def describe(x):
    print("타입: {}".format(x.type()))
    print("크기: {}".format(x.shape))
    print("값: {}".format(x))


x = torch.randn(2, 3)
describe(x)

describe(torch.add(x, x))

describe(x + x)

x = torch.arange(6)
describe(x)

x = x.view(2, 3)
describe(x)

describe(torch.sum(x, dim=0))

describe(torch.sum(x, dim=1))

describe(torch.transpose(x, 0, 1))
