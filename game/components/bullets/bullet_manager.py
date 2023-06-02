import pygame

class BulletManager():
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            self.destroy_player(game, bullet)

        for bullet in self.bullets:
            bullet.update(self.bullets)
            self.destroy_enemy(game, bullet)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 1:
            self.bullets.append(bullet)

    def destroy_player(self, game, bullet):
        if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
            self.enemy_bullets.remove(bullet)
            game.death_count += 1
            game.playing = False
            pygame.time.delay(1000)

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