from game.components.power_ups.power_up import PowerUp
from game.utils.constants import NUKE, NUKE_TYPE
import pygame


class Nuke(PowerUp):
    def __init__(self):
        super().__init__(pygame.transform.scale(NUKE ,(50, 50)), NUKE_TYPE)