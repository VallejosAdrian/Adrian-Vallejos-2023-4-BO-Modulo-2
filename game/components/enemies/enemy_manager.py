import random
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT

class EnemyManager():
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            self.destroy_player_with_nave(game, enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1, 2)

        if enemy_type == 1:
            enemy = Enemy()
        else:
            x_speed = 10
            y_speed = 2
            move_x_for = [1500, 1500]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        
        if len(self.enemies) < 1:
            self.enemies.append(enemy)

    def destroy_player_with_nave(self, game, enemy):
        if enemy.rect.colliderect(game.player.rect):
            game.playing = False
            pygame.time.delay(1000)
        
    def destroy_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []