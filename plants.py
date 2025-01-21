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


class Plant(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.cost = 0  # стоимость
        self.dmg = 0  # урон
        self.cd = 20  # перезарядка для выставления на поле
        self.speed = 0  # скорость действия (стрельба/выдача солнц)
        self.size = 90, 90  # размер

    def update(self):
        pass


class Peashooter(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/gorox_1.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dmg = 50
        self.cost = 100
        self.speed = 10

    # def update(self, shooting=True):
    #     peea = Pea(self.coords, all_sprites) //////не работает
    #     peea.update()


# class Pea(pygame.sprite.Sprite):
#     def __init__(self, coords, *group):
#         super().__init__(*group)
#         self.image = load_image('potatomine.png')
#         self.image = pygame.transform.scale(self.image, (50, 50)) //////не работает
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         self.rect.x += 10


class Sunflower(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/sunflower.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cost = 50
        self.speed = 10

class Wallnut(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/orex.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cd = 50
        self.cost = 50


class Repeater(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/gorox_2.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cost = 200
        self.dmg = 50
        self.speed = 10


class Cherrybomb(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/cherry.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cost = 150
        self.dmg = 600
        self.cd = 100


class Potatomine(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        image = load_image('plants/potatomine.png')
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cost = 25
        self.dmg = 500

