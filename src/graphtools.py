class Graph:
    '''图类'''
    def __init__(self, nums) -> None:
        '''
        初始化
        '''
        self.v_list = [] # 初始化一个顶点列表
        self.mat = [[0]*nums for i in range(nums)] # 初始化一个矩阵以便存放节点信息
        self.v_nums = 0 # 节点个数默认为0
        self.pathstack = [] # 栈存储路径信息
        self.path = [] # 最终输出的路径列表

    def add_vertex(self, v):
        '''
        添加顶点信息
        '''
        if v in self.v_list:
            # 如果v已经存在于顶点列表中，直接return
            return
        if self.v_nums >= len(self.mat):
            # 如果此时顶点个数已经大于或等于节点矩阵的最大值，直接return
            return
        v.v_id = self.v_nums
        # 把节点数量的值赋值给编号
        self.v_list.append(v)
        # 把新节点添加在列表的后面
        self.v_nums += 1
        # 添加后顶点总数加一

    def add_edge(self, from_v, to_v, weight=1):
        '''
        添加边
        :param from_v:起始点
        :param to_v:终止点
        :param weght:权重
        '''
        # 如果节点不存在于顶点列表
        if from_v not in self.v_list:
            self.add_vertex(from_v)
        if to_v not in self.v_list:
            self.add_vertex(to_v)
        # from_v 节点的编号为行号，to_v 节点的编号为列号
        self.mat[from_v.v_id][to_v.v_id] = weight

    def find_v(self, v_id):
        '''
        寻找对应id的顶点
        '''
        if v_id >= 0 or v_id <= self.v_nums:
            # 判断是否存在
            return [_v for _v in self.v_list
                    if _v.v_id == v_id][0]

    def find_all_vertexes(self):
        '''
        找到所有的顶点
        '''
        for _v in self.v_list:
            print(_v)


    def get_weight(self):
        '''
        获取节点之间的权重大小
        '''
        for _v in self.v_list:
            edges = self.mat[_v.v_id]
            for col in range(len(edges)):
                w = edges[col]
                if w != 0:
                    print(_v.v_name, '和', self.v_list[col].v_name, '的距离为：', w)

    def bfs(self, from_v, to_v):
        # 查找与 fv 相邻的节点
        self.find_neighbor(from_v)
        # 临时路径
        lst_path = [from_v]
        # 重复条件：队列不为空
        while len(self.pathstack) != 0:
            # 从队列中一个节点（模拟队列）
            tmp_v = self.pathstack.pop(0)
            # 添加到列表中
            lst_path.append(tmp_v)
            # 是不是目标节点
            if tmp_v.v_id == to_v.v_id:
                self.path.append(lst_path)
                print('找到一条路径', [v_.v_name for v_ in lst_path])
                lst_path.pop()
            else:
                self.find_neighbor(tmp_v)

    def dfs(self, from_v, to_v):
        '''
        深度优先
        '''
        self.path.append(from_v)
        if from_v.v_id != to_v.v_id:
            # 查找与 from_v 节点相连的子节点
            lst = self.find_neighbor_(from_v)
            if lst is not None:
                for tmp_v in lst[::-1]:
                    if tmp_v.v_id == to_v.v_id:
                        self.dfs(tmp_v, to_v)
        print(self.path)        


class Vertex:
    '''
    节点类
    '''
    def __init__(self, name, v_id=0) -> None:
        self.v_id = v_id  # id of vertex
        self.v_name = name  # name of vertex
        self.is_visited = False  # wither vertex is visited

    def __str__(self) -> str:
        return f'[id is {0},name is {1}]'.format(self.v_id, self.v_name)
