import pygame
import random
from Map import mapmat

pygame.init()
def convert(x,y):
    '''把坐标进行转换'''
    return 2*x-1,2*y-1

class Robot():
    '''
    机器人类
    '''
    def __init__(self) -> None:
        self.image = pygame.image.load("./src/robot.jpg")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.x_loc = 185
        self.y_loc = 555
        self.start_x = 1
        self.start_y = 1
        self.map_x = 11
        self.map_y = 1

    def action(self, event, screen):
        '''
        行动
        '''

        if event.key == pygame.K_UP:  # 如果按下的是方向上键
            if not self.is_accessable(mapmat.maplist,self.map_x,self.map_y,face_to=4):
                if self.y_loc > 100:
                    self.y_loc -= 100
                    self.start_y -= 1
                    self.map_x -= 2
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                else:
                    screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向上移动')
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
        elif event.key == pygame.K_DOWN:  # 如果按下的是方向下键
            if not self.is_accessable(mapmat.maplist,self.map_x,self.map_y,face_to=3):
                if self.y_loc < 550:
                    self.y_loc += 100
                    self.start_y += 1
                    self.map_x += 2
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                else:
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                # print('向下移动')
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
        elif event.key == pygame.K_LEFT:  # 如果按下的是方向左键
            if not self.is_accessable(mapmat.maplist,self.map_x,self.map_y,face_to=2):
                if self.x_loc > 200:
                    self.x_loc -= 100
                    self.start_x -= 1
                    self.map_y -= 2
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                else:
                    screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向左移动')
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
        elif event.key == pygame.K_RIGHT:  # 如果按下的是方向右键
            if not self.is_accessable(mapmat.maplist,self.map_x,self.map_y,face_to=1):
                if self.x_loc < 600:
                    self.x_loc += 100
                    self.start_x += 1
                    self.map_y += 2
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                else:
                    screen.blit(self.image, (self.x_loc, self.y_loc))
                # print('向右移动')
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
        elif event.key == pygame.K_SPACE:
            screen.blit(self.image, (self.x_loc, self.y_loc))
        pygame.display.update()

    def is_collided(self, gho1, gho2, screen):
        '''
        判断是否与幽灵相碰
        '''
        if (self.x_loc == gho1.x_loc and self.y_loc == gho1.y_loc) or (
                self.x_loc == gho2.x_loc and self.y_loc == gho2.y_loc):
            return True

    def is_won(self, screen):
        '''
        判断是否胜利
        '''
        return self.x_loc == 685 and self.y_loc == 55

    def sensitor(self, gho1,gho2):
        '''探测器'''
        dis1 = abs(self.start_x-gho1.start_x)+abs(self.start_y-gho1.start_y)
        dis2 = abs(self.start_x-gho2.start_x)+abs(self.start_y-gho2.start_y)
        cold = [0,0]
        if dis1 >= 3:
            cold[0] = 0
        elif dis1 == 2:
            cold[0] = 1
        elif dis1 == 1:
            cold[0] = 2

        if dis2 >= 3:
            cold[1] = 0
        elif dis2 == 2:
            cold[1] = 1
        elif dis2 == 1:
            cold[1] = 2

        return sum(cold)

    def r_move(self, chill, choose_list,screen,event,maplist):
        if event.key == pygame.K_SPACE:
            choose_list2 = []
            if chill == 0:
                up = False
                # 往上走
                if self.start_y < 6:
                    choose_list2.append(['向上', (self.start_x, self.start_y + 1)])
                # 往右走
                if self.start_x < 6:
                    choose_list2.append(['向右', (self.start_x + 1, self.start_y)])
                # 在choose_list2中选择一个，并返回两个信息
                choose = choose_list2[random.randrange(0, len(choose_list2), 1)]
                up = up if choose[1][0] - self.start_x == 1 else True
                if up:
                    if self.is_accessable(maplist,self.start_x,self.start_y,1):
                        if self.y_loc > 100:
                            self.y_loc -= 100
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                        else:
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                    else:
                        if self.is_accessable(maplist,self.start_x,self.start_y,1):
                            if self.x_loc < 600:
                                self.x_loc += 100
                                screen.blit(self.image, (self.x_loc, self.y_loc))
                            else:
                                screen.blit(self.image, (self.x_loc, self.y_loc))
                return choose

            if chill >= 2:  # 左一格
                # 往左走
                if len(choose_list) != 0 and choose_list[-1] == '右':
                    choose_list.pop()
                    choose = ['向左', (self.start_x-1 , self.start_y)]
                    if self.is_accessable(maplist,self.start_x,self.start_y,1):
                        if self.x_loc > 200:
                            self.x_loc -= 100
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                        else:
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                    return choose
                # 往下走
                if len(choose_list) != 0 and choose_list[-1] == '上':
                    choose_list.pop()
                    choose = ['向下', (self.start_x, self.start_y-1)]
                    if self.is_accessable(maplist,self.start_x,self.start_y,1):
                        if self.y_loc < 550:
                            self.y_loc += 100
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                        else:
                            screen.blit(self.image, (self.x_loc, self.y_loc))
                    return choose
            # 原地
            if chill == 1 or (len(choose_list) == 0):
                choose = ['原地', (self.start_x, self.start_y)]
                screen.blit(self.image, (self.x_loc, self.y_loc))
                return choose
            pygame.display.update()
        
    
    def is_accessable(self,maplist,x,y,face_to):
        '''判断是否可以通过'''
        if face_to == 1:
            return maplist[x][y+1]
        elif face_to== 2:
            return maplist[x][y-1]
        elif face_to == 3:
            return maplist[x+1][y]
        elif face_to == 4:
            return maplist[x-1][y]

        
