import random

class NSActionSet:
    """
    Non-shiftable appliances, e.g., refrigerator and alarm system,
    require high reliability to ensure daily-life convenience and safety, 
    so their demands must be satisfied and cannot be scheduled. 
    Therefore, only one action, i.e., “on”, can be taken by the non-shiftable appliance agent.
    """
    def __init__(self):
        self.n = 1
        self.actions = [1]

    def sample(self):
        return random.choice(self.actions)
    

class PSActionSet:
    """
    Power-shiftable appliances, such as air conditioner, heating and light,
    can operate flexibly by consuming energy in a predefined range. 
    Hence, power-shiftable agents can choose discrete actions, i.e., 1, 2, 3,..., 
    which indicate the power ratings at different levels.
    """
    def __init__(self, power_ratings):
        self.n = len(power_ratings)
        self.actions = power_ratings

    def sample(self):
        return random.choice(self.actions)
    

class TSActionSet:
    """
    The time-shiftable loads can be scheduled from peak periods to off-peak periods 
    to reduce the electricity cost and avoid peak energy usage. 
    Time-shiftable appliances, including wash machine and dishwasher, 
    have two operating points, “on” and “off”.
    """
    def __init__(self):
        self.n = 2
        self.actions = [0, 1]

    def sample(self):
        return random.choice(self.actions)
    

class EVActionSet:
    """
    Electric vehicle is a special type of time-shiftable load, 
    which can be charged at different power ratings. 
    """
    def __init__(self, power_ratings):
        self.n = len(power_ratings)
        self.actions = power_ratings

    def sample(self):
        return random.choice(self.actions)
    

class ObservationSet:
    """
    The observation space is defined as the tuple of the current electricity price and the current solar generation. 
    """
    def __init__(self, e_prices, solar, agent):
        self.e_prices = e_prices
        self.solar = solar
        self.agent = agent
        self.n = len(e_prices) + len(solar)
        self.esmin = 0
        self.emax = 20
        self.smax = 80

    def get_states(self):
        all_e = [i for i in range(self.esmin, self.emax + 1)]
        all_s = [i for i in range(self.esmin, self.smax + 1)]
        return (all_e, all_s)