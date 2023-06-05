import random
import pygame
from game.components.enemies.enemy import Enemy
from game.components.explosions.explosion import Explosion
from game.utils.constants import SCREEN_HEIGHT, SHIELD_TYPE

class EnemyManager():
    def __init__(self):
        self.enemies = []
        self.explosions = pygame.sprite.Group()  # Grupo de explosiones

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            self.destroy_player_with_nave(game, enemy)

        self.explosions.update()  # Actualizar todas las explosiones

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        self.explosions.draw(screen)  # Dibujar todas las explosiones

    def add_enemy(self):
        enemy_type = random.randint(1, 2)

        if enemy_type == 1:
            enemy = Enemy()

        else:
            x_speed = 10
            y_speed = 2
            move_x_for = [1500, 1500]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
    
        if len(self.enemies) < 2:
            self.enemies.append(enemy)

    def destroy_player_with_nave(self, game, enemy):
        comparasion = (game.player.power_up_type != SHIELD_TYPE)
        if enemy.rect.colliderect(game.player.rect) and comparasion:
            self.enter_list(enemy)
            game.life_counter -= 1
            if comparasion and game.life_counter < 0:
                self.enter_list(enemy)
                game.death_count += 1
                game.playing = False
                pygame.time.delay(2500)
               
    def destroy_enemy(self, enemy):
        self.enemies.remove(enemy)
        bum = Explosion(enemy.rect.x, enemy.rect.y)
        self.explosions.add(bum)  # Agregar la explosión al grupo de explosiones

    def reset_bomb(self, game):
        enemy_coordinates = [(enemy.rect.x, enemy.rect.y) for enemy in self.enemies]
        self.enemies.clear()

        destroyed_count = len(enemy_coordinates)  # Cantidad de naves destruidas
        game.score += destroyed_count
    
        for x, y in enemy_coordinates:
            bum = Explosion(x, y)
            self.explosions.add(bum)

    def enter_list(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def reset_list(self):
        self.enemies = []