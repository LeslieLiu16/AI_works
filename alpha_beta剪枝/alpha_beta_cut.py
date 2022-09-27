'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-14 17:02:17
LastEditTime: 2022-09-14 20:26:15
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''


class Node:
    '''
    :param value 该节点的值
    :param is_max 判断是否在max层
    :param childnode 子节点列表，其中包含的均为Node类
    '''
    def __init__(self, name=None, value=0, is_max=True) -> None:
        self.name = name
        self.value = value
        self.is_max = is_max
        self.child = None

    def set_child_with_node(self, childs):
        '''
        通过节点类来添加子节点
        '''
        if None is self.child:
            self.child = childs
            return
        for c in childs:
            self.child.append(c)

    def get_all_nodes(self):
        '''
        获取该节点下所有节点列表
        '''
        objlist = []
        for i in self.child:
            objlist.append(i)
            for j in i.child:
                objlist.append(j)
        return objlist


def init():
    '''
    初始化树状结构
    '''
    A = Node(name='A')
    A1 = Node(name='A1', is_max=False)
    A2 = Node(name='A2', is_max=False)
    A3 = Node(name='A3', is_max=False)
    A.set_child_with_node([A1, A2, A3])
    A11 = Node(name='A11', value=3)
    A12 = Node(name='A12', value=2)
    A1.set_child_with_node([A11, A12])
    A21 = Node(name='A21', value=4)
    A22 = Node(name='A22', value=2)
    A23 = Node(name='A23', value=5)
    A2.set_child_with_node([A21, A22, A23])
    A31 = Node(name='A31', value=5)
    A32 = Node(name='A32', value=10)
    A3.set_child_with_node([A31, A32])
    return A


objlist = []


def alpha_beta(node, alpha, beta):
    '''
    alpha表示己方,要提高到最大利益,beta表示敌方,要降到最小利益
    alpha大于beta的时候就可以开始剪枝了,因为己方收益已经可以保证大于敌方收益了
    min层修改beta(最小化敌方收益),max层修改alpha(最大化己方收益)
    '''
    print('正在对', node.name, '进行搜索...')
    if node.child is None:
        print('未找到子节点，进行区间收缩')
        print('--------------------------------------------')
        return node.value
    if not node.is_max:
        # 该层为min层,要最小化敌方收益,所以best_value取越小越好(初始一个无穷大)
        best_value = float('inf')
        for c in node.child:
            value = alpha_beta(c, alpha, beta)
            best_value = min(best_value, value)
            objlist.append(c)
            beta = min(beta, best_value)
            print('对', node.name, '进行操作')
            print('beta的值变为', beta, ',现在的区间为[', alpha, ',', beta, ']')
            print('--------------------------------------------')
            if alpha >= beta:
                break
    else:
        # 该层为max层,要最大化己方收益,所以best_value取越大越好(初始一个无穷小)
        best_value = -float('inf')
        for c in node.child:
            value = alpha_beta(c, alpha, beta)
            best_value = max(best_value, value)
            objlist.append(c)
            alpha = max(alpha, best_value)
            print('对', node.name, '进行操作')
            print('alpha的值变为', alpha, ',现在的区间为[', alpha, ',', beta, ']')
            print('--------------------------------------------')
            if alpha >= beta:
                break
    return best_value


def get_namelist(objlist):
    '''
    获取节点对象的名称
    '''
    namelist = []
    for i in objlist:
        namelist.append(i.name)
    return namelist


def get_cutnodelist(objlist, node):
    '''
    获取所有被剪枝节点的列表
    '''
    cutoff_list = []
    for i in node.get_all_nodes():
        if i.name not in get_namelist(objlist):
            cutoff_list.append(i.name)

    return cutoff_list


def get_final_node(objlist, tree):
    '''
    获取最终选择的节点
    '''
    final = tree.get_all_nodes().pop()
    if final.child is None:
        return final.name
    else:
        get_final_node(objlist)


if __name__ == '__main__':
    tree = init()
    print('alpha-beta剪枝操作完成...', '\n', '剪枝得到最好的值为：',
          alpha_beta(tree, -float('inf'), float('inf')))
    print(' 被剪枝的节点为：', get_cutnodelist(objlist, tree))
    print(' 最终选择的节点为：', get_final_node(objlist, tree))
    print(' 遍历过的节点有：', get_namelist(objlist))
