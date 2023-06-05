import pygame
from pygame.sprite import Sprite
from game.components.explosions.explosion import Explosion
from game.utils.constants import BOMB

class BombBullet(Sprite):
    BOMB = pygame.transform.scale(BOMB, (30, 45))
    SPEED = 10

    def __init__(self, spaceship):
        self.image = self.BOMB
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets, game):
        self.rect.y -= self.SPEED
        if self.rect.y <= 300:
            bullets.remove(self)
            game.bomb_reset()
            game.highest_score.append(game.score)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))