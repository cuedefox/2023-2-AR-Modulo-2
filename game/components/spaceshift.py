from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_DIMENTIONS
import pygame

class Spaceshift(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image ,(SPACESHIP_DIMENTIONS['x'],SPACESHIP_DIMENTIONS['y']))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = 500

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x , self.rect.y))
    
    def move_left(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - SPACESHIP_DIMENTIONS['x']

    def move_right(self):
        self.rect.x += 10
        if self.rect.x > SCREEN_WIDTH - SPACESHIP_DIMENTIONS['x']:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - SPACESHIP_DIMENTIONS['y']:
            self.rect.y += 10