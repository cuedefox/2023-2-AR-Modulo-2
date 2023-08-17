import pygame
import os

# Global Constants
TITLE = "Jala Space Invaders"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/menu.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
NUKE = pygame.image.load(os.path.join(IMG_DIR, 'Other/nuke.png'))
AMMO = pygame.image.load(os.path.join(IMG_DIR, 'Other/ammo.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
NUKE_TYPE = 'nuke'
AMMO_TYPE = 'ammo'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
SPACESHIP_DIMENTIONS = {'x': 40, 'y': 60}

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))
ENEMY_5 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))
EXPLOTION_IMG = pygame.image.load(os.path.join(IMG_DIR, "Other/exp.png"))
ENEMY_TYPES = {
    1: {
        'name': 'ship1',
        'image': ENEMY_1,
        'speed_x': 5,
        'speed_y': 1,
        'score': 50
    },
    2: {
        'name': 'ship2',
        'image': ENEMY_2,
        'speed_x': 3,
        'speed_y': 1,
        'score': 25
    },
    3: {
        'name': 'x-wing',
        'image': ENEMY_3,
        'speed_x': 9,
        'speed_y': 2,
        'score': 75
    },
    4: {
        'name': 'jedi',
        'image': ENEMY_4,
        'speed_x': 8,
        'speed_y': 1,
        'score': 65
    },
    5: {
        'name': 'alien',
        'image': ENEMY_5,
        'speed_x': 3,
        'speed_y': 5,
        'score': 150
    }
}

FONT_STYLE = 'freesansbold.ttf'