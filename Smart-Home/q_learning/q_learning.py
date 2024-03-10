import numpy as np 
import random

class QLearning:
    def __init__(self, env, alpha=0.1, gamma=0.6, epsilon=0.1, epsilon_decay=0.999, epsilon_min=0.01):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
        self.actions = env.action_space.actions
        self.state = 0

    def choose_action(self):
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(self.actions)
        else:
            action = np.argmax(self.q_table[self.state])
        return action

    def learn(self, reward, new_state):
        current_q = self.q_table[self.state, self.action]
        max_future_q = np.max(self.q_table[new_state])
        new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_future_q)
        self.q_table[self.state, self.action] = new_q
        self.state = new_state

    def eps_decay(self):
        self.epsilon = self.epsilon * self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)

    def reset(self, e_prices, solar):
        self.state = 0
        self.env.reset(e_prices, solar)
        self.q_table = np.zeros((self.env.observation_space.n, self.env.action_space.n))