import torch
from torch.utils.data import Dataset
from torchvision import datasets, transforms

class MyDataset(Dataset):

    def __init__(self, train=True):
        super(MyDataset, self).__init__()
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

        self.dataset = datasets.MNIST(root='./data', train=train, download=True, transform=self.transform)
        # train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        image, label = self.dataset[idx]
        return image, label