import torch
import torch.nn as nn
from constants import *

class MyNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(MyNet, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
        self.fc1 = nn.Linear(hidden_size, 64)
        self.activation = nn.GELU()
        self.fc2 = nn.Linear(64, 80)
        self.fc3 = nn.Linear(80, 160)
        self.fc4 = nn.Linear(160, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size, device=DEVICE)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size, device=DEVICE)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc1(out[:, -1, :])
        out = self.activation(out)
        out = self.fc2(out)
        out = self.activation(out)
        out = self.fc3(out)
        out = self.activation(out)
        out = self.fc4(out)
        return out