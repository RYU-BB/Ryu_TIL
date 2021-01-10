"""Loading Data
Use MiniBatch gradient descent to process large amounts of data
"""

from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.nn.functional as f


class CustomDataset(Dataset):
    def __init__(self):
        self.x_data = [[73, 80, 75],
                       [93, 88, 93],
                       [89, 91, 80],
                       [96, 98, 100],
                       [73, 66, 70]]
        self.y_data = [[152], [185], [180], [196], [142]]

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.x_data[idx])
        y = torch.FloatTensor(self.y_data[idx])

        return x, y


dataset = CustomDataset()
data_loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True,
)

model = nn.Linear(3, 1)

optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

epochs = 2000
for epoch in range(epochs + 1):
    for batch_idx, samples in enumerate(data_loader):
        x_train, y_train = samples
        prediction = model(x_train)
        cost = f.mse_loss(prediction, y_train)

        optimizer.zero_grad()
        cost.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print("Epoch {:4d}/{} Cost: {:.6f}".format(
                epoch, epochs, cost.item()
            ))
