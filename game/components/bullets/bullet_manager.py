import pygame

from game.utils.constants import SHIELD_TYPE
from game.utils.constants import ENEMY_TYPES

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.explosion_timer = 0
        self.show_explosion = False
        self.explosion_duration = 1000

    def update(self, game):
        current_time = pygame.time.get_ticks()
        for enemy in game.enemy_manager.enemies:

            if enemy.is_exploding:
                if current_time - enemy.explosion_start_time >= self.explosion_duration:
                    game.score += ENEMY_TYPES[enemy.enemy_type]['score']
                    game.enemy_manager.enemies.remove(enemy)
                continue
        
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    game.sounds['exp'].play()
                    self.enemy_bullets.remove(bullet)
                    game.player.die(game)
                    break
                self.enemy_bullets.remove(bullet)
        
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:

                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullets.remove(bullet)
                    game.sounds['exp'].play()
                    enemy.explode()
                    break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet, game):
        player_max_bullets = 1
        if game.player.power_up_type == 'ammo':
            player_max_bullets = 10
        if bullet.owner == 'enemy' and len (self.enemy_bullets) < 5:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len (self.bullets) < player_max_bullets:
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []