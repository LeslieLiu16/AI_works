from graphtools import Edge, Graph
from searchtools import deepfirstsearch

if __name__ == '__main__':

    graph = Graph(11)
    graph.add_edge(0, 5, 150)
    graph.add_edge(0, 1, 150)
    graph.add_edge(0, 2, 150)
    graph.add_edge(0, 6, 150)
    graph.add_edge(5, 3, 150)
    graph.add_edge(5, 4, 150)
    graph.add_edge(3, 4, 150)
    graph.add_edge(4, 6, 150)
    graph.add_edge(9, 10, 150)

    print(graph.adj)
    searcher = deepfirstsearch(graph, 3)
    print(searcher.is_match(2))
    print(searcher.is_match(3))
    print(searcher.is_match(10))
    print(searcher.counts())

