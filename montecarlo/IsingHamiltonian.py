import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# import montecarlo
import random
import networkx as nx
import random
import scipy
import math
from .BitString import BitString

class IsingHamiltonian:
    def __init__(self, G: nx.Graph, mu) -> None:
        self.graph = G
        self.mu = mu
        self.J = self.graph
    
    
    def energy(self, conf):
        E = 0
        for node in range(conf.N):
            for link in self.graph[node]:
                if link[0]>node:
                    if conf.config[node] == conf.config[link[0]]:
                        E += link[1]
                    else:
                        E -= link[1]
        E += np.dot(self.mu, 2*np.array(conf.config) - 1)
        return E
    
    
    def compute_average_values(self, conf, T):
        E = 0
        M = 0
        E_sq = 0
        M_sq = 0
        P = 0
        for i in range(conf.n_dim):
            conf.set_int_config(i)
            Ei = self.energy(conf)
            Pi = np.exp(-Ei/T)
            E += Ei*Pi
            E_sq += (Ei**2)*Pi
            Mi = np.sum(2*np.array(conf.config) - 1)
            M += Mi*Pi
            M_sq += (Mi**2)*Pi
            P += Pi
        
        E = E/P
        M = M/P
        M_sq = M_sq / P
        E_sq = E_sq / P
        HC = (E_sq - E**2)/(T**2)
        MS = (M_sq - M**2)/T
        
        return E, M, HC, MS
    
    
    
    def energy_diff(self, conf, flip_spin):
        E_del = 0
        for link in self.graph[flip_spin]:
            E_del -= 2 * (2 * conf.config[flip_spin] - 1) * self.mu[flip_spin]
            # if conf.config[flip_spin] == conf.config[node]:
            #     E_del -=  2 * w
            # else:
            #     E_del += 2 * w
            
            E_del -= 2 * (2 * conf.config[flip_spin] - 1)*(2 * conf.config[link[0]] - 1) * link[1]
        return E_del
    
    def mc_step(self, conf, T=1, steps=1, mode = "fast_"):
        if mode == "slow_":
            for step in range(steps):
                for site in range(conf.N):
                # for site in range(len(conf.config)):
                    E1 = self.energy(conf)
                    conf.flip(site)
                    E2 = self.energy(conf)
                    delta_E = E2 - E1
                    W = np.exp(-delta_E/T)
                    accept = True
                    if delta_E >0:
                        r = random.uniform(0, 1)
                        if r<W:
                            accept = True
                        else:
                            accept = False
                    
                    
                    if accept:
                        pass
                    else:
                        conf.flip(site)
        elif mode == "fast_":
            for step in range(steps):
                for site in range(conf.N):
                # for site in range(len(conf.config)):
                    delta_E = self.energy_diff(conf, site)
                    W = np.exp(-delta_E/T)
                    # print(delta_E)
                    accept = True
                    if delta_E >0:
                        r = random.uniform(0, 1)
                        if r<W:
                            accept = True
                        else:
                            accept = False
                    
                    
                    if accept:
                        conf.flip(site)
                    else:
                        pass
        return conf
                    
                    