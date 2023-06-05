import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.bomb import Bomb
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.reset_time_power = self.when_appears
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power_up_type = random.choice(["shield", "bomb_power"])
        if power_up_type == "shield":
            power_up = Shield()
        elif power_up_type == "bomb_power":
            power_up = Bomb()
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
            self.when_appears = current_time + self.reset_time_power

        for power_up in self.power_ups:
            if power_up.type == "shield":
                self.power_shield(game, power_up)
            elif power_up.type == "bomb_power":
                self.power_bomb(game, power_up)

    def power_shield(self, game, power_up):
        power_up.update(game.game_speed, self.power_ups)
        if game.player.rect.colliderect(power_up):
            power_up.star_time = pygame.time.get_ticks()
            game.player.power_up_type = power_up.type
            game.player.has_power_up = True
            game.player.power_time_up = power_up.star_time + (self.duration * 1000)
            game.player.set_image((65, 75), SPACESHIP_SHIELD)
            self.power_ups.remove(power_up)

    def power_bomb(self, game, power_up):
        power_up.update(game.game_speed, self.power_ups)
        if game.player.rect.colliderect(power_up):
            self.power_ups.remove(power_up)
            game.bomb_ammunition += 1

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = pygame.time.get_ticks() + random.randint(5000, 10000)