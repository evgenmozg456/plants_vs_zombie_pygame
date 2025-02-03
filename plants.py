import pygame

import os
import sys
import random


pygame.init()

plant_kill_zombie = 0

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
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/gorox_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/gorox_1.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.last_score_time = pygame.time.get_ticks()
        self.last_score_time1 = pygame.time.get_ticks()
        self.group = group
        self.pea_group = pea_group
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.zombie_group = zombie_group
        self.rect.x = x
        self.rect.y = y
        self.hp = 6
        self.dmg = 50
        self.cost = 100
        self.speed = 10
        self.time_collide = 0

    def update(self):
        for zombie in self.zombie_group:
            if pygame.sprite.collide_mask(self, zombie):
                self.time_collide += 1
                if self.time_collide >= 100:
                    self.hp -= 1
                    self.time_collide = 0
        if self.hp <= 0:
            self.kill()
        current_time1 = pygame.time.get_ticks()
        if current_time1 - self.last_score_time1 >= 2000:
            self.render_pea()
            self.last_score_time1 = current_time1

    def render_pea(self):
        pea = Pea(self.rect.x + self.size[0], self.rect.y, self.zombie_group, self.pea_group)

    def cost_plant(self):
        return self.cost


class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, zombie_group, *group):
        super().__init__(*group)
        self.zombie_group = zombie_group
        self.image = pygame.image.load('plants/pea.png').convert_alpha()
        self.last_score_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 10
        # for zombie in self.zombie_group:
        #     if pygame.sprite.collide_mask(self, zombie):
        #         self.kill()
        # current_time = pygame.time.get_ticks()
        # if pygame.sprite.spritecollideany(self, self.zombie_group):
        #     if current_time - self.last_score_time >= 1000:


class Sunflower(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/podsolnux_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/sunflower.png').convert_alpha()
        self.pea_group = pea_group
        self.image = pygame.transform.scale(self.image, self.size)
        self.last_score_time = pygame.time.get_ticks()
        self.last_score_time1 = pygame.time.get_ticks()
        self.zombie_group = zombie_group
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cost = 50
        self.speed = 10
        self.hp = 6
        self.time_collide = 0

    def update(self):
        for zombie in self.zombie_group:
            if pygame.sprite.collide_mask(self, zombie):
                self.time_collide += 1
                if self.time_collide >= 100:
                    self.hp -= 1
        if self.hp <= 0:
            self.kill()
        current_time1 = pygame.time.get_ticks()
        if current_time1 - self.last_score_time1 >= 17000:
            self.render_sun()
            self.last_score_time1 = current_time1

    def render_sun(self):
        sun = Sun(self.rect.x + self.size[0], self.rect.y, self.pea_group)


class Sun(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('plants/sun.png').convert_alpha()
        self.last_score_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(x - 140, x - 20)
        self.rect.y = y
        self.rect_end = self.rect.y + 20

    def update(self):
        if self.rect.y < self.rect_end:
            self.rect.y += 1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.kill()


class Wallnut(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/orex_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/orex.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.last_score_time = pygame.time.get_ticks()
        self.zombie_group = zombie_group
        self.rect.x = x
        self.rect.y = y
        self.cd = 50
        self.cost = 50
        self.hp = 50
        self.time_collide = 0

    def update(self):
        for zombie in self.zombie_group:
            if pygame.sprite.collide_mask(self, zombie):
                self.time_collide += 1
                if self.time_collide >= 1000:
                    self.hp -= 1
        if self.hp <= 0:
            self.kill()


class Cherrybomb(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/cherrybomb_card.jpg').convert_alpha()
            self.image = pygame.transform.scale(self.image, self.size)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        else:
            self.image = pygame.image.load('plants/cherry.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (300, 300))
            self.rect = self.image.get_rect()
            self.rect.x = x - 100
            self.rect.y = y - 100

        self.zombie_group = zombie_group
        self.last_score_time = pygame.time.get_ticks()
        self.cost = 150
        self.dmg = 600
        self.cd = 100

    def update(self):
        explosion_time = pygame.time.get_ticks()
        if explosion_time - self.last_score_time >= 1000:
            self.kill()
        if pygame.sprite.spritecollideany(self, self.zombie_group):
            pygame.sprite.spritecollide(self, self.zombie_group, dokill=True)
            self.last_score_time = explosion_time


class Potatomine(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        global plant_kill_zombie
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/potatomine_card.jpg').convert_alpha()
        else:
            self.image = pygame.image.load('plants/potatomine.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.zombie_group = zombie_group
        self.last_score_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.cost = 25
        self.dmg = 500
        self.active = True

    def update(self):
        zombies = []
        for zomb in self.zombie_group:
            if pygame.sprite.collide_mask(self, zomb):
                zomb.kill()
                if self.active:
                    if self.rect.y == zomb.rect.y:
                        pygame.sprite.spritecollide(self, self.zombie_group, True)
                    self.image = pygame.image.load('plants/explosion.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, self.size)
                    self.active = False
        if not self.active:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_score_time >= 1500:
                self.kill()
                self.last_score_time = current_time


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
