'''
Author: LeslieLiu16 2596943294@qq.com
Date: 2022-09-27 11:11:34
LastEditTime: 2022-09-27 21:16:00
Copyright (c) 2022 by LeslieLiu16 2596943294@qq.com, All Rights Reserved. 
'''
import pygame
from pygame.sprite import Sprite

pygame.init()


class Robot(Sprite):
    '''
    机器人类
    '''
    def __init__(self) -> None:
        Sprite.__init__(self)
        self.image = pygame.image.load("./src/robot.jpg")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.x_loc = 185
        self.y_loc = 555

    def action(self, event, screen):
        '''
        行动
        '''

        if event.key == pygame.K_UP:  # 如果按下的是方向上键
            if self.y_loc > 100:
                self.y_loc -= 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向上移动')
        elif event.key == pygame.K_DOWN:  # 如果按下的是方向下键
            if self.y_loc < 550:
                self.y_loc += 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向下移动')
        elif event.key == pygame.K_LEFT:  # 如果按下的是方向左键
            if self.x_loc > 200:
                self.x_loc -= 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向左移动')
        elif event.key == pygame.K_RIGHT:  # 如果按下的是方向右键
            if self.x_loc < 600:
                self.x_loc += 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                screen.blit(self.image, (self.x_loc, self.y_loc))
            # print('向右移动')
        pygame.display.update()

    def is_collided(self, gho1, gho2, screen):
        '''
        判断是否与幽灵相碰
        '''
        if (self.x_loc == gho1.x_loc and self.y_loc == gho1.y_loc) or (
                self.x_loc == gho2.x_loc and self.y_loc == gho2.y_loc):
            screen.blit(pygame.image.load('./src/loss.jpg'), (350, 200))

            return True

    def is_won(self, screen):
        '''
        判断是否胜利
        '''
        if self.x_loc == 685 and self.y_loc == 55:
            screen.blit(pygame.image.load('./src/win.jpg'), (250, 180))
        return True