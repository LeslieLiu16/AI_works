from graphtools import Vertex, Graph
from searchtools import uniform_cost_search, greedy_best_first_search,depth_first_search

if __name__ == "__main__":
    # 初始化图对象
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

    # for _ in range(len(graph.mat)):
    #     v_name = input("顶点的名称：")
    #     v = Vertex(v_name)
    #     graph.add_vertex(v)

    # 节点之间的关系
    infos = [(0, 1, 75), (0, 2, 71), (1, 3, 118), (1, 7, 140), (2, 7, 151),
             (7, 9, 80), (7, 8, 99), (3, 4, 111), (4, 5, 70), (5, 6, 75),
             (6, 11, 120), (9, 11, 146), (9, 10, 97), (10, 11, 138),
             (8, 12, 211), (10, 12, 101), (12, 13, 90), (12, 14, 85),
             (14, 15, 142), (15, 16, 92), (16, 17, 87), (14, 18, 98),
             (18, 19, 86)]
    for i in infos:
        v = graph.find_v(i[0])
        v1 = graph.find_v(i[1])
        graph.add_edge(v, v1, weight=i[2])

    # print('--------------')
    # graph.get_weight()
    # print('------------')
    # f_v = graph.find_v(0)
    # t_v = graph.find_v(12)
    # graph.bfs(f_v, t_v)
    # graph.dfs(f_v, t_v)
    # get_neibor(graph, 0)
    greedy_best_first_search(graph, 0, 12)
    # uniform_cost_search(graph, 0, 12)
    # depth_first_search(graph,0,12)
