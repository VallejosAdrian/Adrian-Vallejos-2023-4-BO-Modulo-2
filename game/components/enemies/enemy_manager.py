from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2
from game.utils.constants import SCREEN_HEIGHT

class EnemyManager():
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)
            self.enemy2_remove(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    # Verifica que 'Enemy2' este en la pantalla 
    def enemy2_remove(self, enemy):
        if isinstance(enemy, Enemy2) and enemy.rect.y > SCREEN_HEIGHT:
            self.enemies.remove(enemy)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemy_a = Enemy()
            self.enemies.append(enemy)
            self.enemies.append(enemy_a)

        # Veirfica que 'Enemy2' se ecuentre en la lista, no obstante la añadira
        elif not any(isinstance(enemy, Enemy2) for enemy in self.enemies):
            enemy2 = Enemy2()
            self.enemies.append(enemy2)