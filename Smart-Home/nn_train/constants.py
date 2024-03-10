import torch

DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
END_TIME = 24

class EPrice:
    INPUT_SIZE = 6
    HIDDEN_SIZE = 128
    NUM_LAYERS = 2
    OUTPUT_SIZE = 1
    LEARNING_RATE = 0.001
    EPOCHS = 10
    BATCH_SIZE = 64

class Solar:
    INPUT_SIZE = 6
    HIDDEN_SIZE = 128
    NUM_LAYERS = 4
    OUTPUT_SIZE = 1
    LEARNING_RATE = 0.0000001
    EPOCHS = 500
    BATCH_SIZE = 64

class Data:
    EPRICE_PATH = ''
    SOLAR_PATH = './data/solar/'