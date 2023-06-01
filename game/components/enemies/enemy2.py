import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy2(Sprite):
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
                  600, 650, 700, 750, 800, 850, 900, 950, 1000]
    SPEED_Y = 2
    SPEED_X = 10
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 19)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y 
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movemenet_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movemenet_x(self):
        self.index += 1
        if self.movement_x == 'right' and self.rect.x >= SCREEN_WIDTH - 40:
            self.movement_x = 'left'
            self.index = 0
        elif self.movement_x == 'left' and self.rect.x <= 0:
            self.movement_x = 'right'
            self.index = 0