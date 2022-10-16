import sys
from random import randint
import random
import pygame
import time
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
    for i in range(1, 7):
        for j in range(1, 7):
            pygame.draw.rect(surface=screen,
                             color='black',
                             rect=((i - 1) * 100 + 180, (j - 1) * 100 + 50,
                                   100, 100),
                             width=1)
    pygame.draw.line(surface = screen,color='red',start_pos=(480,50),end_pos=(480,150),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(280,150),end_pos=(380,150),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(280,150),end_pos=(280,250),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(580,150),end_pos=(580,350),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(480,250),end_pos=(580,250),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(280,350),end_pos=(480,350),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(580,350),end_pos=(680,350),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(180,450),end_pos=(280,450),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(380,450),end_pos=(480,450),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(580,450),end_pos=(580,550),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(380,550),end_pos=(380,650),width=8)
    pygame.draw.line(surface = screen,color='red',start_pos=(680,550),end_pos=(780,550),width=8)
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


def main():
    '''主函数'''
    draw_map()
    rob = creat_robot()
    gho1, gho2 = creat_ghost()
    move_list = rob.auto_move(gho1,gho2)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                rob.is_won(screen)
                screen.fill('white')
                draw_map()
                if rob.is_collided(gho1, gho2, screen):
                    break
                else:
                    rob.start_x = move_list[count][0]
                    rob.start_y = move_list[count][1]
                    rob.x_loc = (rob.start_x-1) * 100 + 185
                    rob.y_loc = 655-((rob.start_y) * 100)
                    count+=1
                    screen.blit(rob.image,(rob.x_loc,rob.y_loc))
                    gho1.move(screen)
                    gho2.move(screen)
                    if rob.is_collided(gho1, gho2, screen):
                        screen.blit(pygame.image.load('./src/loss.jpg'), (350, 200))
                        time.sleep(1)
                        screen.fill('white')
                        main()
                    elif rob.is_won(screen):
                        screen.blit(pygame.image.load('./src/win.jpg'), (350, 200))
                        time.sleep(1)
                        screen.fill('white')
                        main()     
        pygame.display.flip()



if __name__ == '__main__':
    main()


