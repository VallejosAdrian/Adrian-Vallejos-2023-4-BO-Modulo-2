import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDHT = SCREEN_WIDTH // 2
    MESSAGE_SPACING = 30

    def __init__(self, message, screen):
        screen.fill((225, 225, 225))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.list_score = [message]

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        y_position = self.HALF_SCREEN_HEIGHT
        for message in self.list_score:
            text = self.font.render(message, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.HALF_SCREEN_WIDHT, y_position))
            screen.blit(text, text_rect)
            y_position += self.MESSAGE_SPACING

    def draw_shield(self, screen, message, x = 550, y = 50, color = (255, 255, 255)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((225, 225, 225))

    def update_message(self, message):
        if len(self.list_score) >= 4:
            self.list_score.pop(0)
        self.list_score.append(message)