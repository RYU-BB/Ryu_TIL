from matplotlib import pyplot as plt

sample_rate = 16000
n_point = 1600
skip_list = [sample_rate * 0.3,
             sample_rate * 0.4,
             sample_rate * 0.21,
             sample_rate * 0.15,
             sample_rate * 0.1,
             sample_rate * 0.09,
             sample_rate * 0.17,
             sample_rate * 0.1]

f = open("input16k.raw", 'r')

for i in range(8):
    data = list()

    for skip in skip_list[i]:
        f.read()

    for n in range(n_point):
        data.append(f.read())

