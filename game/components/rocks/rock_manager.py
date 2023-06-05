import pygame
from game.components.rocks.rock import Rock
from game.components.explosions.explosion import Explosion
from game.utils.constants import SHIELD_TYPE

class RockManager():
    def __init__(self):
        self.rocks = []
        self.explosions = pygame.sprite.Group()

    def update(self, game):
        self.add_rock()

        for rock in self.rocks:
            rock.update(self.rocks)
            self.destroy_player(game, rock)
            self.destroy_rock(game, rock)
        self.explosions.update()

    def draw(self, screen):
        for rock in self.rocks:
            rock.draw(screen)
        self.explosions.draw(screen)
        
    def add_rock(self):
        if len(self.rocks) < 3:
            rock = Rock()
            rock2 = Rock()
            self.rocks.append(rock)
            self.rocks.append(rock2)

    def destroy_player(self, game, rock):
        comparison = (game.player.power_up_type != SHIELD_TYPE)
        if rock.rect.colliderect(game.player.rect) and comparison:
            self.enter_list(rock)
            game.life_counter -= 1
            if comparison and game.life_counter < 0:
                self.enter_list(rock)
                game.death_count += 1
                game.playing = False
                pygame.time.delay(2500)

    def destroy_rock(self, game, rock):
        for bullet in game.bullet_manager.bullets:
            if rock.rect.colliderect(bullet.rect):
                self.rocks.remove(rock)
                game.bullet_manager.bullets.remove(bullet)
                bum = Explosion(rock.rect.x, rock.rect.y)
                self.explosions.add(bum)

    def reset_bomb_coordinates(self):
        rock_coordinates = [(rock.rect.x, rock.rect.y) for rock in self.rocks]
        self.rocks.clear()
    
        for x, y in rock_coordinates:
            bum = Explosion(x, y)
            self.explosions.add(bum)

    def enter_list(self, rock):
        if rock in self.rocks:
            self.rocks.remove(rock)

    def reset(self):
         self.rocks = []
