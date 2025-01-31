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
        self.size = 100, 100  # размер

    def update(self):
        pass


class Peashooter(Plant):
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/gorox_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/gorox_1.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


        self.dmg = 50
        self.cost = 100
        self.speed = 10


    def cost_plant(self):
        return self.cost


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
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/podsolnux_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/sunflower.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.cost = 50
        self.speed = 10

class Wallnut(Plant):
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/orex_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/orex.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


        self.cd = 50
        self.cost = 50


class Repeater(Plant):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('plants/gorox_2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


        self.cost = 200
        self.dmg = 50
        self.speed = 10


class Cherrybomb(Plant):
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/cherrybomb_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/cherry.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


        self.cost = 150
        self.dmg = 600
        self.cd = 100


class Potatomine(Plant):
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/potatomine_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/potatomine.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.cost = 25
        self.dmg = 500


class Shovel(pygame.sprite.Sprite):
    def __init__(self, x, y, card=False, *group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/shovel_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('cards/lopata.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)