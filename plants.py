import pygame


class Plant(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.cost = 0  # стоимость
        self.dmg = 0  # урон ///// у базового зомби 500 хп, а горохострел наносит 50 дмг
        self.cd = 20  # перезарядка для выставления на поле
        self.speed = 0  # скорость действия (стрельба/выдача солнц)
        self.size = 90, 90  # размер
        self.hp = 6  # hp /// количество укусов для удаления растения

    def update(self):
        pass


class Peashooter(Plant):
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.coords = coords
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
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect = coords
        self.cost = 50
        self.speed = 10


class Wallnut(Plant):
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect = coords
        self.cd = 50
        self.cost = 50
        self.hp = 30


class Repeater(Plant):
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect = coords
        self.cost = 200
        self.dmg = 50
        self.speed = 10


class Cherrybomb(Plant):
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect = coords
        self.cost = 150
        self.dmg = 600
        self.cd = 100


class Potatomine(Plant):
    def __init__(self, coords: tuple, image: str, *group):
        super().__init__(*group)
        image = load_image(image)
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect = coords
        self.cost = 25
        self.dmg = 500
