'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-27 14:44:01
LastEditTime: 2022-10-01 14:37:51
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''
import sys
from random import randint
import random
import pygame
from Robot import Robot
from Ghost import Ghost


def init_game():
    '''
    初始化
    '''
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    screen.fill((255, 255, 255))
    pygame.display.set_caption('智闯鬼屋')
    return screen


screen = init_game()


def draw_map():
    '''
    绘制地图
    '''
    arealist = [[None for i in range(8)] for j in range(8)]
    for i in range(1, 7):
        for j in range(1, 7):
            pygame.draw.rect(surface=screen,
                             color='black',
                             rect=((i - 1) * 100 + 180, (j - 1) * 100 + 50,
                                   100, 100),
                             width=1)

            # arealist[i][j] = Area(screen,
            #                       ((i - 1) * 100 + 180 + i * 100 + 180) / 2,
            #                       ((j - 1) * 100 + 50 + j * 100 + 50) / 2)

    img_exit = pygame.image.load("./src/exit.jpg")
    img_exit = pygame.transform.scale(img_exit, (95, 95))
    screen.blit(img_exit, (500 + 180 + 2, 50 + 2))



def creat_robot():
    '''
    绘制robot
    '''
    rob = Robot()
    screen.blit(rob.image, (180 + 5, 500 + 50 + 5))
    return rob


def creat_ghost():
    '''
    绘制幽灵
    '''
    gho1 = Ghost()
    gho2 = Ghost()
    if gho1.start_x == 1 and gho1.start_y == 1:
        gho1.start_y = randint(2, 6)
    elif gho1.start_x == 6 and gho1.start_y == 6:
        gho1.start_y == randint(1, 5)

    if gho2.start_x == 1 and gho2.start_y == 1:
        gho2.start_y = randint(2, 6)
    elif gho2.start_x == 6 and gho2.start_y == 6:
        gho2.start_y == randint(1, 5)

    if gho1.face_to == gho2.face_to or abs(gho1.face_to - gho2.face_to) == 1:
        if gho1.face_to == 1 or gho1.face_to == 2:
            gho2.face_to = random.sample([3, 4], 1)[0]
        elif gho1.face_to == 3 or gho1.face_to == 4:
            gho2.face_to = random.sample([1, 2], 1)[0]

    screen.blit(gho1.image,((gho1.start_x-1) * 100 + 185, 655-((gho1.start_y) * 100)))
    screen.blit(gho2.image,((gho2.start_x-1) * 100 + 185, 655-((gho2.start_y) * 100)))
    return gho1, gho2


if __name__ == '__main__':
    draw_map()
    rob = creat_robot()
    gho1, gho2 = creat_ghost()
    print(rob.sensitor(gho1,gho2))
    trace_list = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                rob.is_won(screen)
                screen.fill('white')
                draw_map()
                # rob.action(event, screen)
                if rob.is_collided(gho1, gho2, screen):
                    break
                else:

                    choose = rob.r_move(rob.sensitor(gho1,gho2),trace_list,screen,event)
                    print(choose)
                    gho1.move(screen)
                    print('幽灵1',gho1.start_x,gho1.start_y)
                    gho2.move(screen)
                    print('幽灵2',gho2.start_x,gho2.start_y)
                    rob.is_won(screen)
                    rob.is_collided(gho1, gho2, screen)
                    robot_last_pos = (rob.start_x,rob.start_y)
                    rob.start_x = choose[1][0]
                    rob.start_y = choose[1][1]
                    print('寒意浓度', rob.sensitor(gho1,gho2))
                    robot_now_pos = (rob.start_x,rob.start_y)
                    if robot_now_pos[0] - robot_last_pos[0] == 1:
                        trace_list.append('右')
                    if robot_now_pos[1] - robot_last_pos[1] == 1:
                        trace_list.append('上')        
        pygame.display.flip()


