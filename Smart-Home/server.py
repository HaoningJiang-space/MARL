import communications
import nn_train
import q_learning
import json
import numpy as np
import schedule
import time

T = 24
config = None

def get_next_data():
    pass

def execute_policy(t, agent, policy):
    pass

def daily_update():
    global config
    with open('config.json','rb') as f:
        config = json.load(f)

    _agents = config.get('agents')
    agents = sorted(_agents, key=lambda x: x.get('alpha', 0), reverse=True)
    episodes = config.get('episodes')
    e_prices = np.zeros(T)
    solar_gen = np.zeros(T)

    for t in range(T):
        e_prices, solar_gen = get_next_data(e_prices, solar_gen) # inclusive
        remain_solar = solar_gen[0]
        
        for agent in agents:
            ql = None
            if agent.get('type') == 'NS':
                ql = q_learning.QLearning(
                    q_learning.Env(agent, e_prices=e_prices, solar=solar_gen, solar_avail=remain_solar)
                    )
            elif agent.get('type') == 'PS':
                ql = q_learning.QLearning(
                    q_learning.Env(agent, power_ratings=agent.get('power_ratings'), e_prices=e_prices, solar=solar_gen, solar_avail=remain_solar)
                    )
            elif agent.get('type') == 'TS':
                ql = q_learning.QLearning(
                    q_learning.Env(agent, e_prices=e_prices, solar=solar_gen, solar_avail=remain_solar)
                    )
            elif agent.get('type') == 'EV':
                ql = q_learning.QLearning(
                    q_learning.Env(agent, power_ratings=agent.get('power_ratings'), e_prices=e_prices, solar=solar_gen, solar_avail=remain_solar)
                    )

            for episode in range(episodes):
                ql.reset(e_prices, solar_gen)
                done = False
                while not done:
                    action = ql.choose_action()
                    next_state, reward, done, info = ql.env.step(action)
                    ql.learn(reward, next_state)
                ql.eps_decay()

            remain_solar = info['remain_solar']
            
            policy = np.zeros(ql.env.observation_space.n)
            for state in ql.env.observation_space.get_states():
                policy[state] = np.argmax(ql.q_table[state])
        
        execute_policy(t, agent, policy)

if __name__ == '__main__':
    schedule.every().day.at("00:00").do(daily_update)
    while True:
        schedule.run_pending()
