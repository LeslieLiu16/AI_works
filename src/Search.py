'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-07 18:05:48
LastEditTime: 2022-09-10 21:17:44
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''
from Graph import *


class Search:
    '''
    定义搜索类
    '''
    def __init__(self, graph) -> None:
        self.graph = graph  # 定义图变量
        self.stack = []
        self.path = []

    def depth_first_search(self, from_vertex, to_vertex):
        '''
        深度优先搜索方法
        '''
        from_vertex.is_visited = True
        # self.path.append(from_vertex.name)
        neibors = self.graph.get_neibors(from_vertex)

        for neibor in neibors:
            self.stack.append(self.graph.find_vertex(neibor))

        for neibor in self.stack:
            if not neibor.is_visited:
                self.path.append(neibor.name)
                self.depth_first_search(neibor, to_vertex)
            else:
                continue


    def breadth_first_search(self, from_vertex, to_vertex):
        '''
        广度优先搜索算法
        '''
        from_vertex.is_visited = True
        # self.path.append(from_vertex.name)
        neibors = self.graph.get_neibors(from_vertex)

        for neibor in neibors:
            self.stack.append(self.graph.find_vertex(neibor))

        for neibor in self.stack:
            if not neibor.is_visited:
                self.path.append(neibor.name)
                self.depth_first_search(neibor, to_vertex)
            else:
                continue

    def greedy_best_first_search(self, from_vertex, to_vertex):
        '''
        最短距离的贪婪最佳优先搜索
        '''

        # from_ver = self.graph.find_vertex(from_vertex)
        # to_ver = self.graph.find_v(to_vertex)
        # path = [from_ver.v_name]
        # if to_ver.idx != from_ver.idx:
        #     w_list, id_list = self.graph.get_neibor(from_vertex)
        #     idx = w_list.index(min(w_list))
        #     # print(id_list,w_list,sep=' ')
        #     name_v_id = id_list[idx]
        #     # print(name_v_id)
        #     name = self.graph.find_v(name_v_id)
        #     path.append(name.name)
        #     print(path[0], path[1], sep='->')
        #     self.greedy_best_first_search(from_v=name.idx, to_vertex)
        # print(path_)

    def uniform_cost_search(self, from_vertex, to_vertex):
        '''
        一致代价搜索方法
        '''

        neibors = self.graph.get_neibors(from_vertex)

        for n in neibors:
            w = self.graph.find_vertex(n)
            self.stack.append(self.graph.get_weight(from_vertex, w))

        self.stack.sort()
        print(self.stack[0])
        from_vertex = self.graph.find_vertex(
            self.graph.matrix.index(self.stack[0])[0])
        self.uniform_cost_search(from_vertex, to_vertex)
