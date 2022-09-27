'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-07 16:49:01
LastEditTime: 2022-09-10 21:18:16
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''

from Graph import Graph, Vertex
from Search import Search

if __name__ == '__main__':

    graph = Graph(20)
    # 添加顶点
    names = [
        'Zerind', 'Arad', 'Oradea', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta',
        'Sibiu', 'Fagaras', 'Riminicu Vilces', 'Pitesti', 'Craiova',
        'Bucharest', 'Glurgiu', 'Urziceni', 'Vasful', 'iasi', 'Neatmt',
        'Hirsova', 'Eforie'
    ]

    for _name in names:
        v = Vertex(_name)
        graph.add_vertex(v)

    infos = [(0, 1, 75), (0, 2, 71), (1, 3, 118), (1, 7, 140), (2, 7, 151),
             (7, 9, 80), (7, 8, 99), (3, 4, 111), (4, 5, 70), (5, 6, 75),
             (6, 11, 120), (9, 11, 146), (9, 10, 97), (10, 11, 138),
             (8, 12, 211), (10, 12, 101), (12, 13, 90), (12, 14, 85),
             (14, 15, 142), (15, 16, 92), (16, 17, 87), (14, 18, 98),
             (18, 19, 86)]
    for i in infos:
        v = graph.find_vertex(i[0])
        v1 = graph.find_vertex(i[1])
        graph.add_edge(v, v1, weight=i[2])

    print(graph.matrix)
    # print(len(graph.matrix))
    # graph.add_vertex(0)
    # print(graph.get_weight(0,12))
    # print(graph.get_weight(0,1))
    # v = graph.find_vertex(0)
    # v1 = graph.find_vertex(12)

    # print(graph.get_neibors(v))
    # search = Search(graph=graph)
    # search.uniform_cost_search(from_vertex=v, to_vertex=v1)
    # search.greedy_best_first_search(from_vertex=v, to_vertex=v1)
    # search.depth_first_search(from_vertex=v, to_vertex=v1)
