'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-07 16:30:23
LastEditTime: 2022-09-07 18:50:18
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''


class Graph:
    '''
    定义图数据结构
    '''
    def __init__(self, vertex_nums) -> None:
        self.vertex_num = 0  # 定义图中节点的个数
        self.vertex_list = []  # 初始化一个顶点列表
        self.matrix = [[-1] * vertex_nums
                       for i in range(vertex_nums)]  # 初始化一个连接矩阵

    def add_vertex(self, vertex):
        '''
        添加顶点
        '''
        if vertex in self.vertex_list:
            # 如果列表中已经存在了该位置的索引，则直接return
            return
        if self.vertex_num >= len(self.matrix):
            # 如果顶点的个数已经大于或等于矩阵能存放的值，则直接return
            return
        vertex.idx = self.vertex_num  # 让添加的序号为当前存在的顶点数量的值
        self.vertex_list.append(vertex)  # 把该节点放入顶点列表中
        self.vertex_num += 1

    def add_edge(self, from_vertex, to_vertex, weight=-1):
        '''
        添加边的方法

        :param from_vertex:起始点的编号
        :param to_vertex:终止点的编号
        :param weight:权重,默认为1
        '''
        # 如果节点不存在于节点列表
        if from_vertex not in self.vertex_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            self.add_vertex(to_vertex)
        # 把权重赋值到连接矩阵中
        self.matrix[from_vertex.idx][to_vertex.idx] = weight

    def find_vertex(self, vertex_idx):
        '''
        找到对应索引的顶点,并返回这个顶点对象
        '''
        # 如果这个顶点的索引在范围内
        if vertex_idx >= 0 or vertex_idx <= self.vertex_num:
            # 遍历所有的顶点
            for _v in self.vertex_list:
                # 如果顶点的索引和目标索引一致，则返回该顶点
                if _v.idx == vertex_idx:
                    return _v

    def get_weight(self, from_vertex, to_vertex):
        '''
        查询两个节点之间的权重,并返回
        '''
        # 直接返回连接矩阵中对应位置的值即可
        return self.matrix[from_vertex.idx][to_vertex.idx]

    def get_neibors(self, vertex):
        '''
        找到顶点的子节点
        '''
        # 创建一个邻居列表
        neibors = []
        # 在行中寻找
        for col in range(len(self.matrix[vertex.idx][:])):
            if self.matrix[vertex.idx][col] != -1:
                neibors.append(col)
        # 在列中寻找
        for row in range(len(self.matrix[:][vertex.idx])):
            if self.matrix[row][vertex.idx] != -1:
                neibors.append(row)
        # 排序所有的结构
        neibors.sort()
        return neibors


class Vertex():
    '''
    定义顶点类
    '''
    def __init__(self, name, idx=0) -> None:
        self.idx = idx  # 这是顶点的序号
        self.name = name  # 这是顶点的名称
        self.is_visited = False  # 这是顶点是否被访问
