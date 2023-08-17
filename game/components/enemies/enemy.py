import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_TYPES, EXPLOTION_IMG

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 10
    X_POS = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    MOV_X = {0: 'left', 1: 'right'}
    def __init__(self):
        self.enemy_type = random.randint(1, 5)
        self.image = ENEMY_TYPES[self.enemy_type]['image']
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS[random.randint(0,10)]
        self.speed_x = ENEMY_TYPES[self.enemy_type]['speed_x']
        self.speed_y = ENEMY_TYPES[self.enemy_type]['speed_y']
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.shooting_time = random.randint(300, 500)
        self.type = 'enemy'
        self.is_exploding = False
        self.explosion_start_time = 0

    def update(self, ships, game):
        if self.is_exploding:
            return
        self.rect.y += self.speed_y
        self.shoot(game)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet, game)
            game.sounds['shoot'].play()
            self.shooting_time += random.randint(300, 500)

    def explode(self):
        self.image = pygame.transform.scale(EXPLOTION_IMG ,(40, 60))
        self.is_exploding = True
        self.explosion_start_time = pygame.time.get_ticks()