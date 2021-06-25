import torch


def describe(x):
    print("타입: {}".format(x.type()))
    print("크기: {}".format(x.shape))
    print("값: {}".format(x))


print(torch.cuda.is_available())

device = torch.device("coda" if torch.cuda.is_available() else "cpu")
print(device)

x = torch.rand(3, 3).to(device)
describe(x)

y = torch.rand(3, 3)
cpu_device = torch.device("cpu")
y = y.to(cpu_device)
x = x.to(cpu_device)
print(x + y)