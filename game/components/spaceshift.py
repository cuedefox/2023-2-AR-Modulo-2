from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_DIMENTIONS, DEFAULT_TYPE, EXPLOTION_IMG
import pygame

class Spaceshift(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image ,(SPACESHIP_DIMENTIONS['x'],SPACESHIP_DIMENTIONS['y']))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = 500
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.is_death = False
        self.death_start_time = 0

    def update(self, user_input, game):
        if not self.is_death:
            if user_input[pygame.K_LEFT]:
                self.move_left()
            elif user_input[pygame.K_RIGHT]:
                self.move_right()
            elif user_input[pygame.K_UP]:
                self.move_up()
            elif user_input[pygame.K_DOWN]:
                self.move_down()
            elif user_input[pygame.K_SPACE]:
                game.sounds['shoot'].play()
                self.shoot(game)

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

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet, game)

    def set_image(self, size = (SPACESHIP_DIMENTIONS['x'], SPACESHIP_DIMENTIONS['y']), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image ,size)

    def die(self, game):
        self.is_death = True
        game.death_count+=1
        self.image = pygame.transform.scale(EXPLOTION_IMG ,(40, 60))
        self.death_start_time = pygame.time.get_ticks()

    def reset(self):
        self.is_death = False
        self.image = pygame.transform.scale(SPACESHIP ,(SPACESHIP_DIMENTIONS['x'],SPACESHIP_DIMENTIONS['y']))