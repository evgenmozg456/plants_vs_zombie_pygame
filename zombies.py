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
    def __init__(self, x, y, *group, plants_group, pea_group):
        super().__init__(*group)
        self.image = load_image('zombie1.png')
        self.plants_group = plants_group
        self.pea_group = pea_group
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.stop = False
        self.rect.x = x
        self.rect.y = y
        self.hp = 500

    def update(self):
        # if not pygame.sprite.spritecollideany(self, self.plants_group):
        for plant in self.plants_group:
            if pygame.sprite.collide_mask(self, plant):
                self.stop = True
            elif not pygame.sprite.collide_mask(self, plant):
                self.stop = False
        if not self.stop:
            self.rect.x -= 1
        for pea in self.pea_group:
            if pygame.sprite.collide_mask(self, pea):
                pygame.sprite.spritecollide(self, self.pea_group, dokill=True)
                self.hp -= 100
        if self.hp < 0:
            self.kill()


class ZombieSecond(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 1000


class ZombieThird(Zombie):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 2000
