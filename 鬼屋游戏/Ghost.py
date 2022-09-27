from random import randint
from pygame.sprite import Sprite
import pygame


class Ghost():
    '''
    幽灵类
    '''
    def __init__(self):
        Sprite.__init__(self)
        self.start_x = randint(0, 5)
        self.start_y = randint(0, 5)
        self.face_to = randint(1, 4)  # 有四个方向
        self.image = pygame.transform.scale(
            pygame.image.load('./src/Ghost.jpg'), (90, 90))
        self.x_loc = self.start_x * 100 + 185
        self.y_loc = self.start_y * 100 + 55

    def move(self, screen):
        '''
        移动
        '''
        if self.face_to == 1:
            if self.x_loc < 600:
                self.x_loc += 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                self.face_to = 2
                self.move(screen)

        elif self.face_to == 2:
            if self.x_loc > 200:
                self.x_loc -= 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                self.face_to = 1
                self.move(screen)
        
        elif self.face_to == 3:
            if self.y_loc < 550:
                self.y_loc += 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                self.face_to = 4
                self.move(screen)

        elif self.face_to == 4:
            if self.y_loc > 100:
                self.y_loc -= 100
                screen.blit(self.image, (self.x_loc, self.y_loc))
            else:
                self.face_to = 3
                self.move(screen)

        pygame.display.update()



    def cold(self):
        '''
        降低周围区域的温度
        '''
        pass