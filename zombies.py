import pygame

import os
import sys

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Zombie(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 0  # 😭только хп


class ZombieFirst(Zombie):
    def __init__(self, *group):
        image = load_image('zombie/zombie1.png')
        self.rect = image.get_rect()
        super().__init__(*group)
        self.hp = 500


class ZombieSecond(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 1000


class ZombieThird(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 2000
