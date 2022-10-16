class Map:
    '''
    地图类
    '''

    def __init__(self) -> None:
        self.maplist = [[False for i in range(13)] for j in range(13)]
        
    def set_wall(self,x,y):
        '''设置墙'''
        self.maplist[x][y] = True

    def is_wall(self,x,y):
        '''判断该位置是否有墙'''
        return self.maplist[x][y]
    

global mapmat
mapmat = Map()
mapmat.set_wall(1,6)
mapmat.set_wall(2,3)
mapmat.set_wall(3,2)
mapmat.set_wall(3,8)
mapmat.set_wall(4,7)
mapmat.set_wall(5,8)
mapmat.set_wall(6,3)
mapmat.set_wall(6,5)
mapmat.set_wall(6,9)
mapmat.set_wall(8,1)
mapmat.set_wall(8,5)
mapmat.set_wall(9,8)
mapmat.set_wall(10,11)
mapmat.set_wall(11,4)
print(mapmat.is_wall(8,1))
