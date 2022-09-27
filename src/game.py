'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-14 16:45:45
LastEditTime: 2022-09-14 16:57:15
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''
from Graph import *

def max_value(state, game, alpha, beta):
    if cutoff_test(state):
        return eval(state)
    for s in successors(state):
        alpha = max(alpha, min_value(s, game, alpha, beta))
        if alpha>=beta:
            print('α of ', state, '' is: '', beta)
            return beta

    print('α of ', state, ' is: ', α)

    return alpha

 

def min_value(state, game, alpha, beta):
    if cutoff_test(state):
        return eval(state)
    for s in successors(state):
        beta = min(beta, max_value(s, game, alpha, beta))
        if beta<=alpha:
            print('β of ', state, ' is: ', alpha)
            return alpha

    print('β of ', state, ' is: ', beta)

    return beta

def cutoff_test(state):
    

if __name__ == '__main__':
    state = 'A'
    game = Graph(11)
    alpha = float('inf')
    beta = -float('inf')
    value = max_value(state, game, alpha, beta)
