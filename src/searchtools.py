from graphtools import Graph


def greedy_best_first_search(graph, from_v, to_v):
    '''
    最短距离的贪婪最佳优先搜索
    '''

    from_ver = graph.find_v(from_v)
    to_ver = graph.find_v(to_v)
    path = [from_ver.v_name]
    if to_ver.v_id != from_ver.v_id:
        w_list, id_list = get_neibor(graph=graph, ver=from_v)
        idx = w_list.index(min(w_list))
        # print(id_list,w_list,sep=' ')
        name_v_id = id_list[idx]
        # print(name_v_id)
        name = graph.find_v(name_v_id)
        path.append(name.v_name)
        print(path[0],path[1],sep='->')
        greedy_best_first_search(graph=graph, from_v=name.v_id, to_v=to_v)
    
    # print(path_)

def get_neibor(graph, ver):
    '''
    获取v节点的相邻节点
    '''
    w_list = []
    id_list = []
    v = graph.find_v(ver)
    edge = graph.mat[v.v_id]
    for col in range(len(edge)):
        w = edge[col]
        if w != 0:
            w_list.append(w)
            id_list.append(col)
    return w_list, id_list


def uniform_cost_search(graph, from_v, to_v):
    '''
    一致代价
    '''
    from_ver = graph.find_v(from_v)
    to_ver = graph.find_v(to_v)
    min_num = 0
    path = [from_ver.v_name]
    if to_ver.v_id != from_ver.v_id:
        w_list, id_list = get_neibor(graph=graph, ver=from_v)
        idx = w_list.index(min(w_list))
        name_v_id = id_list[idx]
        name = graph.find_v(name_v_id)
        min_num = min(w_list) + min_num
        for i in w_list:
            if min_num < i:
                path.append(name.v_name)
                uniform_cost_search(graph=graph, from_v=name.v_id, to_v=to_v)
                
            else:
                min_num = i
                path.append(graph.find_v(
                                        id_list[w_list.index(i)]).v_name)
                uniform_cost_search(graph=graph,
                                    from_v=graph.find_v(
                                        id_list[w_list.index(i)]).v_id,
                                    to_v=to_v)
    print(path)


def depth_first_search(graph,from_v,to_v):
    from_ver = graph.find_v(from_v)
    to_ver = graph.find_v(to_v)

    _,id_list = get_neibor(graph,from_v)
    if not id_list:
        for ids in id_list:
            ids_v = graph.find_v(ids)
            if ids_v.v_id != to_ver.v_id:
                print(ids_v.v_name)
                depth_first_search(graph,ids_v.v_id,to_v)

def breadth_first_scearch(graph,from_v,to_v):
    pass