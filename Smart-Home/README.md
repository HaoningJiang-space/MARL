# A Multi-Agent Reinforcement Learning Approach for Home Energy Management

## Project Structure

```
.
├── README.md
├── data
│   ├── solar
│   │   ├── *.csv
│   ├── e_price
│   │   ├── *.csv
│   └── README.md
├── models
│   └── *.pth
├── nn_train
│   ├── __init__.py
│   ├── constants.py
│   ├── net.py
│   ├── predict.py
│   ├── preprocess.py
│   └── train.py
├── q_learning
│   ├── __init__.py
│   ├── env.py
│   ├── q_learning.py
│   └── space.py
├── communications
│   ├── __init__.py
│   └── send_actions.py
├── LICENSE
└── requirements.txt
```

`data`: contains the data used for training and testing the models.

`models`: contains the trained models.

`nn_train`: contains the code for training the neural network.

`q_learning`: contains the code for the Q-learning algorithm.

`communications`: contains the code for the communication between devices.

## How to run