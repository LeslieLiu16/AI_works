import sys
import time
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
    img_exit = pygame.image.load("E:\Program\人工智能技术基础作业\鬼屋游戏\problemA\src\exit.jpg")
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


def main():
    '''主函数'''
    draw_map()
    rob = creat_robot()
    gho1, gho2 = creat_ghost()
    # print(rob.sensitor(gho1,gho2))
    move_list = rob.auto_move(gho1,gho2)
    # print(move_list)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                rob.is_won()
                screen.fill('white')
                draw_map()
                # rob.action(event, screen)
                if rob.is_collided(gho1, gho2):
                    break
                else:
                    rob.start_x = move_list[count][0]
                    rob.start_y = move_list[count][1]
                    rob.x_loc = (rob.start_x-1) * 100 + 185
                    rob.y_loc = 655-((rob.start_y) * 100)
                    count+=1
                    screen.blit(rob.image,(rob.x_loc,rob.y_loc))
                    gho1.move(screen)
                    # print('幽灵1',gho1.start_x,gho1.start_y)
                    gho2.move(screen)
                    # print('幽灵2',gho2.start_x,gho2.start_y)
                    if rob.is_won():
                        time.sleep(1)
                        screen.fill('white')
                        main()
                    elif rob.is_collided(gho1, gho2):
                        time.sleep(1)
                        screen.fill('white')
                        main()
                    # print('寒意浓度', rob.sensitor(gho1,gho2))      
        pygame.display.flip()


if __name__ == '__main__':
    main()


