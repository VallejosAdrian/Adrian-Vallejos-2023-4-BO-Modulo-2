import pygame

class ExplosionManager:
    def __init__(self):
        self.explosions = []

    def update(self):
        for explosion in self.explosions:
            explosion.update(self.explosions)

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, explosion):
        self.explosions.append(explosion)