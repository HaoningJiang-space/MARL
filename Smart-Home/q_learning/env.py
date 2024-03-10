from space import *
from .. import nn_train as nt

class Env:
    def __init__(self, agent, n=0, power_ratings=[], e_prices=[], solar=[], solar_avail=0):
        self.action_space = None
        self.solar_avail = solar_avail
        self.observation_space = ObservationSet(e_prices, solar, agent)
        self.cur_step = 0
        self.n_step = 24
        self.agent = agent
        self.power = agent.get('maxpow')
        if agent.get('type') == 'NS':
            self.action_space = NSActionSet()
        elif agent.get('type') == 'PS':
            self.action_space = PSActionSet(power_ratings)
        elif agent.get('type') == 'TS':
            self.action_space = TSActionSet()
        elif agent.get('type') == 'EV':
            self.action_space = EVActionSet(power_ratings)
        else:
            raise ValueError('Invalid agent type')
        
    def reset(self, e_prices, solar):
        self.cur_step = 0
        self.observation_space.e_prices = e_prices
        self.observation_space.solar = solar

    def step(self, action):
        assert self.action_space.contains(action)
        self.cur_step += 1
        done = self.cur_step >= self.n_step
        res = nt.predict(self.observation_space.e_prices, self.observation_space.solar, 0)
        self.observation_space.e_prices = res[0]
        self.observation_space.solar = res[1]
        next_state = (res[0], res[1])
        info = {}
        reward = -2147483648
        self.power = self.action_space.actions[action] * self.agent.get('maxpow')
        if self.agent.get('type') == 'NS':
            if self.solar_avail >= self.power:
                info['remain_solar'] = self.solar_avail - self.power
                reward = 0
            else:
                info['remain_solar'] = 0
                reward = -self.e_prices[self.cur_step - 1] * (self.power - self.solar_avail)
        elif self.agent.get('type') == 'PS':
            if self.solar_avail >= self.power:
                info['remain_solar'] = self.solar_avail - self.power
                reward = - self.agent.get('alpha', 0) * (self.agent.get('maxpow') - self.power) ** 2
            else:
                info['remain_solar'] = 0
                reward = -self.e_prices[self.cur_step - 1] * (self.power - self.solar_avail) - self.agent.get('alpha', 0) * (self.agent.get('maxpow') - self.power) ** 2
        elif self.agent.get('type') == 'TS':
            pass

