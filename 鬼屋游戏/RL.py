import pandas as pd
import random
import time

#########参数
epsilon = 0.9   # 贪婪度 greedy
alpha = 0.1     # 学习率
gamma = 0.8     # 奖励递减值

#####探索者的状态，即其可到达的位置，有6个len('-o---T')。所以定义
states = range(6)           # 状态集。从0到5
actions = ['left', 'right'] # 动作集。也可添加动作'none'，表示停留
rewards = [0,0,0,0,0,1]     # 奖励集。只有最后的宝藏所在位置才有奖励1，其他皆为0

q_table = pd.DataFrame(data=[[0 for _ in actions] for _ in states],
                       index=states, columns=actions)
