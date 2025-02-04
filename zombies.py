import pygame
from random import choice

pygame.init()


class Zombie(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('zombies/zombie1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hp = 0  # только хп
        self.speed = choice([1, 1, 1, 1, 1, 2])  # скорость зомби в отношении 5:1


class ZombieFirst(Zombie):
    def __init__(self, x, y, *group, plants_group, pea_group):
        super().__init__(*group)
        self.image = pygame.image.load('zombies/zombie_anim/frame_00_delay-0.1s.png').convert_alpha()
        self.plants_group = plants_group
        self.pea_group = pea_group
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.stop = False
        self.rect.x = x
        self.rect.y = y
        self.speed = choice([1, 1, 1, 1, 2, 2])
        self.hp = 500
        self.last_anim_time = pygame.time.get_ticks()
        self.frame_n = 0

    def update(self):
        if self.frame_n < 10:
            self.image = pygame.image.load(f'zombies/zombie_anim/frame_0{self.frame_n}_delay-0.1s.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))
        else:
            self.image = pygame.image.load(f'zombies/zombie_anim/frame_{self.frame_n}_delay-0.1s.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))
        self.frame_n += 1
        if self.frame_n > 50:
            self.frame_n = 0
        for plant in self.plants_group:
            if pygame.sprite.collide_mask(self, plant):
                if plant.rect.y >= self.rect.y:
                    self.stop = True
        if not self.stop:
            self.rect.x -= self.speed
        for pea in self.pea_group:
            if pygame.sprite.collide_mask(self, pea):
                pygame.sprite.spritecollide(self, self.pea_group, dokill=True)
                self.hp -= 100
        if self.hp <= 0:
            self.kill()
