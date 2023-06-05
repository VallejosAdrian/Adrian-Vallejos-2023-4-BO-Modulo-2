import pygame
from pygame.sprite import Sprite
from game.utils.constants import BURST_1, BURST_2, BURST_3, BURST_4

class Explosion(Sprite):
    FRAME_DURATION = 100

    def __init__(self, x, y):
        super().__init__()
        self.images = [BURST_1, BURST_2, BURST_3, BURST_4]
        self.frame_index = 0
        self.frame_timer = pygame.time.get_ticks()
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.frame_timer >= self.FRAME_DURATION:
            self.frame_timer = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
