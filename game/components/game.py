import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, MUSIC, BURST_1
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.rocks.rock_manager import RockManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.enemies.enemy import Enemy
from game.components.menu import Menu
from game.components.lives import Life


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0
        self.life_counter = 3
        self.score = 0
        self.highest_score = [0]
        self.bomb_ammunition = 0
        self.life = Life()
        self.ship_enemy = Enemy()
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.rock_manager = RockManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu('Press Any Key To Star...', self.screen)

    def execute(self):
        MUSIC.set_volume(0.25)
        MUSIC.play()
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()        

    def run(self):
    # Game loop: events - update - draw
        self.reset_all()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.rock_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.rock_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.life.draw(self.screen, self.life_counter)
        self.draw_power_up_time()
        self.draw_score()
        self.draw_highest_score()
        self.draw_bomb_ammunition()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_widht = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_count > 0:
            self.update_list()

        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, (half_screen_widht - 50, half_screen_height - 150))

        self.menu.draw(self.screen)
        self.menu.update(self)

    def update_score(self):
        self.score += 1
        self.highest_score.append(self.score)
    
    def draw_counter_states(self, text, text_rect_center):
        font = pygame.font.Font(FONT_STYLE, 30)
        rendered_text = font.render(text, True, (255, 255, 255))
        text_rect = rendered_text.get_rect()
        text_rect.center = text_rect_center
        self.screen.blit(rendered_text, text_rect)

    def draw_score(self):
        text = f'Score: {self.score}'
        self.draw_counter_states(text, (1000, 50))

    def draw_highest_score(self):
        text = f'Top Score: {max(self.highest_score)}'
        self.draw_counter_states(text, (1000, 80))

    def draw_bomb_ammunition(self):
        text = f'Bomb Ammunition: {self.bomb_ammunition}'
        self.draw_counter_states(text, (550, 580))

    def bomb_reset(self):
        self.enemy_manager.reset_bomb(self)
        self.bullet_manager.reset()
        self.rock_manager.reset_bomb_coordinates()

    def reset_all(self):
        self.score = 0
        self.bomb_ammunition = 0
        self.life_counter = 3
        self.enemy_manager.reset_list()
        self.bullet_manager.reset()
        self.rock_manager.reset()
        self.player.reset()
        self.power_up_manager.reset()

    def update_list(self):
        self.menu.update_message(f'Game Over. Press Any Key To Star :)')
        self.menu.update_message(f'Your Score: {str(self.score).zfill(3)}')
        self.menu.update_message(f'Higthest Score: {str(max(self.highest_score)).zfill(3)}')
        self.menu.update_message(f'Total Deaths: {str(self.death_count).zfill(3)}')

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.menu.draw_shield(self.screen, f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show} seconds')
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
