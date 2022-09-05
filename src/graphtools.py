class Graph():
    '''图类'''
    vertice = 0  # 顶点数量
    edge = 0  # 边数量
    adj = []  # 邻接表

    def __init__(self, vertice) -> None:
        '''
        初始化
        '''
        self.vertice = vertice
        self.edge = 0
        self.adj = [{} for i in range(vertice)]

    def get_vertice(self) -> int:
        '''
        获取顶点数
        '''
        return self.vertice

    def get_edge(self) -> int:
        '''
        获取边数
        '''
        return self.edge

    def add_edge(self, vertice1, vertice2, length):
        '''
        建立连接边
        :param vertice1:起始顶点
        :param vertice2:结束顶点
        :param length:边长度
        '''
        self.adj[vertice1].update({vertice2: length})
        self.adj[vertice2].update({vertice1: length})
        # self.adj.insert(vertice1, {vertice2: length})
        # self.adj.insert(vertice2, {vertice1: length})
        self.edge = self.edge + 1

    def get_near_vertice(self, vertice):
        '''
        获取该顶点的所有相邻顶点
        :param vertice: 指定一个顶点
        '''
        return self.adj[vertice]


class Edge():
    '''边类'''
    nextnode = ''  # 子节点的名字 next node
    prvsnode = ''  # 父节点的名字 previous node
    distance = 0  # 边的长度

    def __init__(self, nextnode, prvsnode, distance) -> None:
        '''
        初始化
        :param nextnode:下一节点
        :param prvsnode:上一节点
        :param distance:两节点之间的距离
        :return:无
        '''
        self.nextnode = nextnode
        self.prvsnode = prvsnode
        self.distance = distance

    def set_nextnode(self, nextnode_name):
        '''
        设置下一节点，（子节点）
        :param nextnode_name: 子节点名
        '''
        self.nextnode = nextnode_name

    def set_prvsnode(self, prvsnode_name):
        '''
        设置上一节点，（父节点）
        :param prvsnode_name: 父节点名
        '''
        self.prvsnode = prvsnode_name

    def set_distance(self, distance):
        '''
        设置边的长度
        :param:distance:设置边的长度
        '''
        self.distance = distance
