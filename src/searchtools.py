from graphtools import Graph


class deepfirstsearch:

    is_searched = []
    count = 0
    graph = None

    def __init__(self, graph, vertice) -> None:
        '''
        初始化
        '''
        self.is_searched = [False for i in range(graph.get_vertice())]
        self.count = 0
        self.graph = graph
        self.dfs(graph, vertice)

    def dfs(self, graph, vertice):
        '''
        dfs实现
        '''
        self.is_searched[vertice] = True
        for dics in graph.adj:
            for key in dics.keys():
                if not self.is_searched[key]:
                    self.dfs(graph, key)
                    
        self.count = self.count + 1

    def is_match(self, vertice):
        '''
        输出与该节点节点是否可以相连
        '''
        return self.is_searched[vertice]

    def counts(self):
        '''
        输出与该节点相连的节点数
        '''
        return self.count



        