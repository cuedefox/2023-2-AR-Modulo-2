from game.components.power_ups.power_up import PowerUp
from game.utils.constants import AMMO, AMMO_TYPE
import pygame


class Ammo(PowerUp):
    def __init__(self):
        super().__init__(pygame.transform.scale(AMMO ,(50, 50)), AMMO_TYPE)