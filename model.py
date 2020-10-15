import torch


class ActionClassifier(torch.nn.Module):
    def __init__(self):
        super(ActionClassifier, self).__init__()
        self.features = torch.nn.Sequential(
            torch.nn.Conv2d(3, 12, 3),
            torch.nn.BatchNorm2d(12),
            torch.nn.ReLU(),
            torch.nn.Conv2d(12, 48, 3),
            torch.nn.BatchNorm2d(48),
            torch.nn.ReLU(),
            torch.nn.Conv2d(48, 96, 3),
            torch.nn.BatchNorm2d(96),
            torch.nn.ReLU()
        )
        self.classifier = torch.nn.Linear(1, 2)

    def forward(self, x):
        x = self.features(x)
        x = x.view(-1, 1)
        print(x.shape)
        out = self.classifier(x)
        return out
