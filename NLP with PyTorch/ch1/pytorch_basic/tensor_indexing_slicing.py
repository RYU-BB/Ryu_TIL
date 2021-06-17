import torch


def describe(x):
    print("타입: {}".format(x.type()))
    print("크기: {}".format(x.shape))
    print("값: {}".format(x))


x = torch.arange(6).view(2, 3)
describe(x)

describe(x[:1, :2])

describe(x[0, 1])

indices = torch.LongTensor([0, 2])
describe(torch.index_select(x, dim=1, index=indices))

indices = torch.LongTensor([0, 0])
describe(torch.index_select(x, dim=0, index=indices))

row_indices = torch.arange(2).long()
col_indices = torch.LongTensor([0, 1])
describe(x[row_indices, col_indices])

x = torch.arange(6).view(2, 3)
describe(x)

describe(torch.cat([x, x], dim=0))

describe(torch.cat([x, x], dim=1))

describe(torch.stack([x, x]))

x1 = torch.arange(6).view(2, 3)
describe(x1)

x2 = torch.ones(3, 2)
x2[:, 1] += 1
describe(x2)

describe(torch.mm(x1, x2))
