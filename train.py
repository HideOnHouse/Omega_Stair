import torch
from matplotlib import pyplot as plt
from utils import do, get_screen_information
from time import sleep

from model import ActionClassifier
from torch.utils.data import DataLoader, Dataset


def main():
    start, climb, switch = get_screen_information()
    model = ActionClassifier()
    model.cuda()
    model.train()

    optimizer = torch.optim.AdamW(model.parameters())
    criterion = torch.nn.CrossEntropyLoss()
    while True:
        x = torch.tensor(do(switch))
        prediction = model(x)
        loss = criterion
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


if __name__ == '__main__':
    main()
