import sys
from time import sleep
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
    for i in range(6):
        for j in range(6):
            pygame.draw.rect(surface=screen,
                             color='black',
                             rect=(i * 100 + 180, j * 100 + 50, 100, 100),
                             width=1)
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
    while (gho1.start_x == 5 and gho1.start_y == 5) or (gho1.start_x == 0
                                                        and gho1.start_y == 0):
        del gho1
        gho1 = Ghost()
    screen.blit(gho1.image,
                (gho1.start_x * 100 + 185, gho1.start_y * 100 + 55))
    while (gho2.start_x == 5 and gho2.start_y == 5) or (gho2.start_x == 0
                                                        and gho2.start_y == 0):
        while gho1.start_x == gho2.start_x and gho1.start_y == gho2.start_y:
            del gho2
            gho2 = Ghost()
    screen.blit(gho2.image,
                (gho2.start_x * 100 + 185, gho2.start_y * 100 + 55))
    return gho1, gho2


if __name__ == '__main__':
    draw_map()
    rob = creat_robot()
    gho1, gho2 = creat_ghost()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                rob.is_won(screen)
                screen.fill('white')
                draw_map()
                rob.action(event, screen)
                if rob.is_collided(gho1, gho2, screen):
                    break
                else:
                    gho1.move(screen)
                    gho2.move(screen)
                    rob.is_collided(gho1, gho2, screen)
                    rob.is_won(screen)

        pygame.display.flip()
