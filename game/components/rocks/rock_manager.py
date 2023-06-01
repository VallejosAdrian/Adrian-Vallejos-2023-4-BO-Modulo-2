import pygame
from game.components.rocks.rock import Rock

class RockManager():
    def __init__(self):
        self.rocks = []


    def update(self, game):
        self.add_rock()

        for rock in self.rocks:
            rock.update(self.rocks)
            self.destroy_player(game, rock)
            self.destroy_rock(game, rock)

    def draw(self, screen):
        for rock in self.rocks:
            rock.draw(screen)
        
    def add_rock(self):
        if len(self.rocks) < 1:
            rock = Rock()
            rock_2 = Rock()
            self.rocks.append(rock)
            self.rocks.append(rock_2)

    def destroy_player(self, game, rock):
        if rock.rect.colliderect(game.player.rect):
                game.playing = False
                pygame.time.delay(1000)

    def destroy_rock(self, game, rock):
        for bullet in game.bullet_manager.bullets:
                if rock.rect.colliderect(bullet.rect):
                    game.bullet_manager.bullets.remove(bullet)
                    self.rocks.remove(rock)
