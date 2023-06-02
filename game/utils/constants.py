import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

ROCK_1 = pygame.image.load(os.path.join(IMG_DIR, "Other/rock1.png"))
ROCK_2 = pygame.image.load(os.path.join(IMG_DIR, "Other/rock2.png"))
ROCK_3 = pygame.image.load(os.path.join(IMG_DIR, "Other/rock3.png"))
ROCK_4 = pygame.image.load(os.path.join(IMG_DIR, "Other/rock4.png"))

BURST_1 = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion00.png"))
BURST_2 = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion01.png"))
BURST_3 = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion02.png"))
BURST_4 = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion03.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
