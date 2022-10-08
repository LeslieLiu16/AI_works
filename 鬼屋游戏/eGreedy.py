import random
import numpy as np

class eGreedy():

    def __init__(self,r,K,count,tries,e) -> None:
        self.r = r
        self.K = K
        self.count = count
        self.tries = tries
        self.e = e
        self.reward
        self.Q = 
    
    def e_greedy(self):
        if random.random() < self.e:
            k = random.uniform(1,self.K)
        else:
            np.argmax()

        