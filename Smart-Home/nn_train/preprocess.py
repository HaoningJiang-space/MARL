import pandas as pd 
import os 
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from constants import *

def get_e_price_data():
    pass

def get_solar_data():
    if not os.path.isdir(Data.SOLAR_PATH):
        raise Exception('Invalid solar path')
    files = os.listdir(Data.SOLAR_PATH)
    if len(files) == 0:
        raise Exception('No solar data found')
    
    features = []
    labels = []
    
    for file in files:
        print(f'Processing {file}...')
        data = []
        infos = file.split('_')
        if infos[0] != 'Actual':
            continue
        latitude = float(infos[1])
        longtitude = float(infos[2])
        year = int(infos[3])
        tp = 0
        if infos[4] == 'UPV':
            tp = 1
        elif infos[4] == 'DPV':
            tp = 0
        else:
            raise Exception('Invalid solar type')
        cap = int(infos[5].split('MW')[0])
        interval = int(infos[6])
        df = pd.read_csv(Data.SOLAR_PATH + file)

        window_size = int(60/interval)
        for i in range(0, len(df) - window_size):
            window = df.iloc[i:i+window_size]
            mean_power = window['Power(MW)'].mean()
            data.append([latitude, longtitude, year, tp, cap, mean_power])

        for i in range(len(data) - END_TIME):
            features.append(data[i:i+END_TIME])
            labels.append(data[i+END_TIME][-1])

    train_size = int(0.8 * len(features))
    
    train_features = torch.tensor(features[:train_size])
    train_labels = torch.tensor(labels[:train_size])

    test_features = torch.tensor(features[train_size:])
    test_labels = torch.tensor(labels[train_size:])

    train_dataset = TensorDataset(train_features, train_labels)
    test_dataset = TensorDataset(test_features, test_labels)

    train_loader = DataLoader(train_dataset, batch_size=Solar.BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=Solar.BATCH_SIZE, shuffle=True)

    return train_loader, test_loader
