import torch


def describe(x):
    print("타입: {}".format(x.type()))
    print("크기: {}".format(x.shape))
    print("값: {}".format(x))


x = torch.ones(2, 2, requires_grad=True)
describe(x)
print(x.grad is None)

y = (x * 2) * (x + 5) + 3
describe(y)
print(x.grad is None)

z = y.mean()
describe(z)
z.backward()
print(x.grad is None)