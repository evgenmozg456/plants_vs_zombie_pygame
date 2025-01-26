import pygame

import os
import sys
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('zombies', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Zombie(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('zombie1.png')
        self.rect = self.image.get_rect()
        self.hp = 0  # 😭только хп


class ZombieFirst(Zombie):
    def __init__(self, x, y, *group, plants_group):
        super().__init__(*group)
        self.image = load_image('zombie1.png')
        self.group = plants_group
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 500

    def update(self):
        if not pygame.sprite.spritecollideany(self, self.group):
            self.rect.x -= 1


class ZombieSecond(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 1000


class ZombieThird(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 2000
