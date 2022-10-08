'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-10-01 16:11:20
LastEditTime: 2022-10-01 18:25:04
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''

import numpy as np
reward = {1:-1,2:-1,3:3}

def Qi(action):
    '''奖励函数'''
    reward = {1:-1,2:-1,3:3}
    return reward.get(action)

def Bolztmann():
    # print(list(reward.values()))
    return np.random.choice(list(reward.keys()))
    # return np.exp(Qi(k)/tao) / np.sum(np.exp(1/tao))


class Softmax():
    
    def __init__(self,K,T) -> None:
        self.K = K
        self.T = T
        self.Q = 0
        self.count = 0
        
    def softmax(self):
        r = 0
        for t in range(self.T):
            k = Bolztmann()
            v = Qi(k)
            r = r + v

            self.Q = (self.Q * self.count + v)/(self.count + 1)
            self.count += 1
        return r


if __name__ == '__main__':

    soft = Softmax(3,20)
    print(soft.softmax())