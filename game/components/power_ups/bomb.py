import pygame
import random
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BOMB_POWER, SCREEN_HEIGHT

class Bomb(PowerUp):
    def __init__(self):
        self.image = pygame.transform.scale(BOMB_POWER, (50, 50))
        self.speed_x = 2
        self.movement_x = random.choice([-3, 3]) * self.speed_x
        self.distance_x = random.randint(80, 90)
        self.current_distance_x = 0
        super().__init__(self.image, 'bomb_power')
    
    def update(self, game_spedd, power_ups):
        self.rect.y += 6
        self.rect.x += self.movement_x

        self.current_distance_x += abs(self.movement_x)

        if self.current_distance_x >= self.distance_x:
            self.movement_x = -self.movement_x
            self.current_distance_x = 0

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)