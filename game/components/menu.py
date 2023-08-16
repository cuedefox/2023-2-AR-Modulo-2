import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

    def __init__(self, message, screen, game):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.stats = self.font.render(f'Best Score: {game.best_score} Deaths: {game.death_count}', True, (0, 0, 0))
        self.stats_rect = self.stats.get_rect()
        self.stats_rect.center = (self.HALF_SCREEN_WIDTH, (self.HALF_SCREEN_HEIGHT + 200))

    def update(self, game):
        self.stats = self.font.render(f'Best Score: {game.best_score} - Deaths: {game.death_count}', True, (0, 0, 0))
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.stats, self.stats_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def reset_screen_color(self, screen):
        screen.fill((255,255,255))