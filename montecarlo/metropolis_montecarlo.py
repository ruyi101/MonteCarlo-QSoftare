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
from .IsingHamiltonian import IsingHamiltonian

def metropolis_montecarlo(ham, conf, T=1, nsweep=8000, nburn=2000, mode = "fast_"):
    conf = ham.mc_step(conf, T, nburn, mode = mode)
    E = np.zeros(nsweep)
    M = np.zeros(nsweep)
    E_sq = np.zeros(nsweep)
    M_sq = np.zeros(nsweep)
    for step in range(nsweep):
        conf = ham.mc_step(conf, T, mode = mode)
        
        Ei = ham.energy(conf)

        E[step] = (E[step - 1] * step + Ei)/(step+1)
        
        E_sq[step] = (E_sq[step - 1] * step + (Ei)**2)/(step+1)
        
        Mi = np.sum(2*np.array(conf.config) - 1) 
        
        M[step] = (M[step - 1] * step + Mi)/(step+1)
        
        M_sq[step] = (M_sq[step - 1] * step + Mi**2)/(step+1)
        
    return E, M, E_sq, M_sq