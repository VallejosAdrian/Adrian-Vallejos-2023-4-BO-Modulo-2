import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, ROCK_1, ROCK_2, ROCK_3, ROCK_4, SCREEN_HEIGHT

class Rock(Sprite):
    Y_POS = 0
    X_POS_LIST = [200, 250, 300, 350, 400, 450, 500, 550,
                  600, 650, 700, 750, 800, 850, 900]
    ROCK_LIST = {0: ROCK_1, 1: ROCK_2, 2: ROCK_3, 3: ROCK_4}
    
    SPEED_Y = 7
    SPEED_X = 3
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self):
      self.image = self.ROCK_LIST[random.randint(0, 3)]
      self.image = pygame.transform.scale(self.image, (50, 60))
      self.rect = self.image.get_rect()
      self.rect.x = self.X_POS_LIST[random.randint(0, 14)]
      self.rect.y = self.Y_POS
      self.speed_x = self.SPEED_X
      self.speed_y = self.SPEED_Y
      self.movement_x = self.MOV_X[random.randint(0, 1)]
      self.index = 0

    def update(self, rocks):
        self.rect.y += self.speed_y
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        if self.rect.y >= SCREEN_HEIGHT:
            rocks.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

