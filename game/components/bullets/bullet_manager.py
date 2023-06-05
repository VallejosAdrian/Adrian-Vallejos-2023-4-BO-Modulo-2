import pygame
from game.utils.constants import SHIELD_TYPE

class BulletManager():
    def __init__(self):
        self.bomb_list = []
        self.bullets = []
        self.enemy_bullets = []
        self.shoot_interval = 300
        self.last_shot_time = 0

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            self.destroy_player(game, bullet)

        for bullet in self.bullets:
            bullet.update(self.bullets)
            self.destroy_enemy(game, bullet)

        for bullet in self.bomb_list:
            bullet.update(self.bomb_list, game)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.bomb_list:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 2:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time >= self.shoot_interval:
                self.bullets.append(bullet)
                self.last_shot_time = current_time
                
    def add_bomb(self, bullet):
        self.bomb_list.append(bullet)

    def destroy_player(self, game, bullet):
        comparison = (game.player.power_up_type != SHIELD_TYPE)
        if (bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy') and comparison:
            self.enemy_bullets.remove(bullet)
            game.life_counter -= 1
            if comparison and game.life_counter < 0:
              game.death_count += 1
              game.playing = False
              pygame.time.delay(2500)

    def destroy_enemy(self, game, bullet):
        # Itera sobre la lista de enemigos, para ver si colisiona o no 
        for enemy in game.enemy_manager.enemies:
            if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                self.bullets.remove(bullet)
                game.enemy_manager.destroy_enemy(enemy)
                game.update_score()
                
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
        self.bomb_list = []