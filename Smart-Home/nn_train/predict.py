from train import *

e_price_model = MyNet(EPrice.INPUT_SIZE, EPrice.HIDDEN_SIZE, EPrice.NUM_LAYERS, EPrice.OUTPUT_SIZE).to(DEVICE)
solar_model = MyNet(Solar.INPUT_SIZE, Solar.HIDDEN_SIZE, Solar.NUM_LAYERS, Solar.OUTPUT_SIZE).to(DEVICE)

def load_model(model_name):
    e_price_model.load_state_dict(torch.load(f'../models/{model_name[0]}'))
    solar_model.load_state_dict(torch.load(f'../models/{model_name[1]}'))

def predict_e_price_single(inputs):
    return e_price_model(inputs).squeeze().item()

def predict_solar_single(inputs):
    return solar_model(inputs).squeeze().item()

def predict(e_inputs, s_inputs, end_time=END_TIME):
    e_outputs = []
    s_outputs = []

    for i in range(end_time + 1):
        e_outputs.append(predict_e_price_single(e_inputs))
        s_outputs.append(predict_solar_single(s_inputs))
        e_inputs = torch.cat((e_inputs[1:], torch.tensor([e_outputs[-1]])))
        s_inputs = torch.cat((s_inputs[1:], torch.tensor([s_outputs[-1]])))

    return e_outputs, s_outputs

def predict_main(model_name, e_inputs, s_inputs):
    load_model(model_name)
    return predict(e_inputs, s_inputs)