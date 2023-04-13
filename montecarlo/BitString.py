import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# import montecarlo
import random
import networkx as nx
import random
import scipy
import math


class BitString:
    """
    Simple class to implement a string of bits
    """
    def __init__(self, N):
        self.string = np.zeros(N)
        
        self.config = self.string
        self.N = N
        self.n_dim = 2**N

    def __str__(self):
        real_str = ''
        for i in range(len(self.string)):
            real_str += str(self.string[i])
        return real_str 
        
    def __len__(self):
        return len(self.string)
    
    # def __eq__(self, other):
    #     if self.string == other.string:
    #         return True
    #     else:
    #         return False
    

    def flip(self, position):
        self.string[position] = (self.string[position] + 1)%2
        self.config = self.string
        

        
        
        
    def set_config(self, list):
        self.string = list
        self.config = list
        
    def on(self):
        on_num = 0
        for i in range(len(self.string)):
            if self.string[i] == 1:
                on_num += 1
        return on_num
    
    def off(self):
        off_num = 0
        for i in range(len(self.string)):
            if self.string[i] == 0:
                off_num += 1
        return off_num
    
    def int(self):
        num = 0
        for i in range(len(self.string)):
            num += 2**(len(self.string)-i-1) * self.string[i]
            # num += 2**(i) * self.string[i]
        return num
    
    def set_int_config(self, num, digits = -1):
        res = num
        digits = self.N
        if digits == -1:
            digits = int(np.log2(res)) + 1
            new_str = [0]* digits
            for i in range(digits):
                new_str[i] = res // 2**(digits - i - 1)
                res = res - new_str[i] * 2**(digits - i - 1)
            
            self.string = new_str
            self.config = new_str
        
        else:
            new_str = [0]* digits
            for i in range(digits):
                new_str[i] = res // 2**(digits - i - 1)
                res = res - new_str[i] * 2**(digits - i - 1)
            
            self.string = new_str
            self.config = new_str
    
    
    def initialize(self, M=0, verbose=0):
        """
        Initialize spin configuration with specified magnetization
        
        Parameters
        ----------
        M   : Int, default: 0
            Total number of spin up sites 
        """
        self.config = np.zeros(self.N, dtype=int) 
        randomlist = random.sample(range(0, self.N), M)
        for i in randomlist:
            self.config[i] = 1
        
        self.string = self.config