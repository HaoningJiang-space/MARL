import torch
import torch.nn as nn
from constants import *
from net import MyNet
from preprocess import get_e_price_data, get_solar_data
from matplotlib import pyplot as plt

class Train:
    def __init__(self, model, train_loader, test_loader, criterion, optimizer, epochs):
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader
        self.criterion = criterion
        self.optimizer = optimizer
        self.epochs = epochs

    def train(self, generate_figure=True):
        for epoch in range(self.epochs):
            train_losses = []
            test_losses = []
            for i, (features, labels) in enumerate(self.train_loader):
                features = features.to(DEVICE)
                labels = labels.to(DEVICE)
                outputs = self.model(features)
                loss = self.criterion(outputs.squeeze(), labels)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                train_losses.append(loss.item())

            with torch.no_grad():
                for i, (features, labels) in enumerate(self.test_loader):
                    features = features.to(DEVICE)
                    labels = labels.to(DEVICE)
                    outputs = self.model(features)
                    loss = self.criterion(outputs.squeeze(), labels)
                    test_losses.append(loss.item())

            print(f'Epoch {epoch+1}/{self.epochs}, train loss: {sum(train_losses)/len(train_losses)}, test loss: {sum(test_losses)/len(test_losses)}')

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model


def main(target, input_size, hidden_size, num_layers, output_size, learning_rate, epochs):
    model = MyNet(input_size, hidden_size, num_layers, output_size).to(DEVICE)
    train_loader, test_loader = None, None
    if target == 'e_price':
        train_loader, test_loader = get_e_price_data()
    elif target == 'solar':
        train_loader, test_loader = get_solar_data()
    else:
        raise Exception('Invalid target')
    print('>>> Data loaded <<<')
    print(f'Number of training samples: {len(train_loader.dataset)}')
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    trainer = Train(model, train_loader, test_loader, criterion, optimizer, epochs)
    trainer.train()
    torch.save(trainer.get_model().state_dict(), f'./models/model_{target}_{learning_rate}_{epochs}.pth')
    print('>>> Model saved <<<')

if __name__ == '__main__':
    # main('e_price', EPrice.INPUT_SIZE, EPrice.HIDDEN_SIZE, EPrice.NUM_LAYERS, EPrice.OUTPUT_SIZE, EPrice.LEARNING_RATE, EPrice.EPOCHS)
    main('solar', Solar.INPUT_SIZE, Solar.HIDDEN_SIZE, Solar.NUM_LAYERS, Solar.OUTPUT_SIZE, Solar.LEARNING_RATE, Solar.EPOCHS)
