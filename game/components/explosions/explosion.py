import pygame
from pygame.sprite import Sprite
from game.utils.constants import BURST

class Explosion(Sprite):
    def __init__(self, rect):
        self.image = pygame.transform.scale(BURST, ( 50, 50))
        self.rect = self.image.get_rect(center=rect.center)
        self.timer = 0
        self.duration = 1000 

    def update(self, explosions):
        self.timer += pygame.time.get_ticks()
        if self.timer >= self.duration:
            explosions.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)