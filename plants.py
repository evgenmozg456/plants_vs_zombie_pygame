import pygame

import random


class Plant(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.hp = 6  # количество укусов для съедения
        self.size = 100, 100  # размер

    def update(self):
        pass


class Peashooter(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/gorox_card.jpg').convert_alpha()
        else:
            self.image = (
                pygame.image.load(f'plants/peashooter_anim/frame_00_delay-0.1s.png').convert_alpha())
        self.image = pygame.transform.scale(self.image, self.size)
        self.last_time_to_shoot = pygame.time.get_ticks()
        self.pea_group = pea_group
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.zombie_group = zombie_group
        self.rect.x = x
        self.rect.y = y
        self.hp = 6
        self.time_collide = 0
        self.frame_n = 0
        self.time_to_anim = 0

    def update(self):
        if self.time_to_anim >= 5:
            if self.frame_n < 10:
                self.image = (
                    pygame.image.load(f'plants/peashooter_anim/frame_0{self.frame_n}_delay-0.1s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            else:
                self.image = (
                    pygame.image.load(f'plants/peashooter_anim/frame_{self.frame_n}_delay-0.1s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            self.frame_n += 1
            if self.frame_n > 23:
                self.frame_n = 0
            self.time_to_anim = 0
        self.time_to_anim += 1
        for zombie in self.zombie_group:
            if pygame.sprite.collide_mask(self, zombie):
                self.time_collide += 1
                if self.time_collide >= 100:
                    self.hp -= 1
                    self.time_collide = 0
        if self.hp <= 0:
            self.kill()
        time_to_shoot = pygame.time.get_ticks()
        if time_to_shoot - self.last_time_to_shoot >= 2000:
            self.render_pea()
            self.last_time_to_shoot = time_to_shoot

    # функция создаёт пулю-горошину
    def render_pea(self):
        pea = Pea(self.rect.x + self.size[0], self.rect.y, self.zombie_group, self.pea_group)


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


class Sunflower(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/podsolnux_card.jpg').convert_alpha()
        else:
            self.image = (
                pygame.image.load(f'plants/sunflower_anim/frame_00_delay-0.03s.png').convert_alpha())
        self.pea_group = pea_group
        self.image = pygame.transform.scale(self.image, self.size)
        self.time_to_spawn_sun = pygame.time.get_ticks()
        self.zombie_group = zombie_group
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 6
        self.time_collide = 0
        self.frame_n = 0
        self.time_to_anim = 0

    def update(self):
        if self.time_to_anim >= 2:
            if self.frame_n < 10:
                self.image = (
                    pygame.image.load(f'plants/sunflower_anim/frame_0{self.frame_n}_delay-0.03s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            else:
                self.image = (
                    pygame.image.load(f'plants/sunflower_anim/frame_{self.frame_n}_delay-0.03s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            self.frame_n += 1
            if self.frame_n > 54:
                self.frame_n = 0
            self.time_to_anim = 0
        self.time_to_anim += 1
        for zombie in self.zombie_group:
            if pygame.sprite.collide_mask(self, zombie):
                self.time_collide += 1
                if self.time_collide >= 100:
                    self.hp -= 1
        if self.hp <= 0:
            self.kill()
        time_to_spawn_sun = pygame.time.get_ticks()
        if time_to_spawn_sun - self.time_to_spawn_sun >= 15000:
            self.render_sun()
            self.time_to_spawn_sun = time_to_spawn_sun

    # функция создаёт солнышко
    def render_sun(self):
        sun = Sun(self.rect.x + self.size[0], self.rect.y, self.pea_group)


class Sun(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('plants/sun.png').convert_alpha()
        self.kill_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(x - 120, x - 10)
        self.rect.y = y
        self.rect_end = self.rect.y + 30
        self.kill_time = pygame.time.get_ticks()

    def update(self):
        if self.rect.y < self.rect_end:
            self.rect.y += 1
        live_time = pygame.time.get_ticks()
        if live_time - self.kill_time >= 2000:
            self.kill()


class Wallnut(Plant):
    def __init__(self, x, y, card=False, *group, zombie_group, pea_group):
        super().__init__(*group)
        if card:
            self.image = pygame.image.load('cards/orex_card.jpg').convert_alpha()
        else:
            self.image = (
                pygame.image.load(f'plants/wallnut_anim/frame_00_delay-0.05s.png').convert_alpha())
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.zombie_group = zombie_group
        self.rect.x = x
        self.rect.y = y
        self.hp = 50
        self.time_collide = 0
        self.frame_n = 0
        self.time_to_anim = 0

    def update(self):
        if self.time_to_anim >= 5:
            if self.frame_n < 10:
                self.image = (
                    pygame.image.load(f'plants/wallnut_anim/frame_0{self.frame_n}_delay-0.05s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            else:
                self.image = (
                    pygame.image.load(f'plants/wallnut_anim/frame_{self.frame_n}_delay-0.05s.png').convert_alpha())
                self.image = pygame.transform.scale(self.image, (100, 100))
            self.frame_n += 1
            if self.frame_n > 43:
                self.frame_n = 0
            self.time_to_anim = 0
        self.time_to_anim += 1
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
            self.image = pygame.image.load(f'plants/cherry_anim/frame_00_delay-0.1s.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (300, 300))
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x - 100
            self.rect.y = y - 100

        self.zombie_group = zombie_group
        self.last_score_time = pygame.time.get_ticks()
        self.cost = 150
        self.frame_n = 0

    def update(self):
        if self.frame_n < 10:
            self.image = pygame.image.load(f'plants/cherry_anim/frame_0{self.frame_n}_delay-0.1s.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (300, 300))
            self.rect.x = self.x - 100
            self.rect.y = self.y - 100
        else:
            self.image = pygame.image.load(f'plants/cherry_anim/frame_{self.frame_n}_delay-0.1s.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (300, 300))
        self.frame_n += 1
        if self.frame_n > 30:
            self.kill()
        if pygame.sprite.spritecollideany(self, self.zombie_group):
            pygame.sprite.spritecollide(self, self.zombie_group, dokill=True)


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
