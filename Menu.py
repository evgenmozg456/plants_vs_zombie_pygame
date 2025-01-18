from winreg import SetValueEx

import pygame
import os
import sys


class Menu(pygame.sprite.Sprite):
    def __init__(self, name, screen, x, y, sound, colorkey=None):
        self.name = name
        self.screen = screen
        self.x = x
        self.y = y
        self.changer = True
        self.buttton_sound = pygame.mixer.Sound(sound)
        self.back = 0
    def render(self):
        self.left = width // 4

    def load_image(self, name):
        fullname = os.path.join('images_main_menu', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        self.all_sprites = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(fullname)
        self.all_sprites.add(self.sprite)
        return self.sprite.image

    def background(self):
        # КНОПКА ИГРАТЬ

        # self.sprite.image = pygame.transform.scale(self.sprite.image, (
        # self.sprite.image.get_width() // 5, self.sprite.image.get_height() // 5))
        fon = pygame.transform.scale(self.load_image('menu.jpg'), (
            width, height))
        survival = pygame.transform.scale(self.load_image('survival_button3.png'), (
            width, height))
        screen.blit(fon, (0, 0))
        screen.blit(survival, (0, 0))
        pygame.display.flip()

        # self.survival_mask = pygame.mask.from_surface(survival)

        # self.sprite.rect = self.sprite.image.get_rect()
        # screen.fill((200, 200, 200))
        # self.all_sprites.draw(screen)

    def but(self):
        # self.area = pygame.Polygon([[640, 200], [1150, 265], [1120, 360], [650, 295]])
        # pygame.draw.polygon(self.screen, (255, 255, 255), [[640, 200], [1150, 265], [1120, 360], [650, 295]], 1 )
        # pygame.draw.cirlce(self.screen, (255, 255, 255), (640, 200, 510, 95), 1)
        # pygame.draw.rect(self.screen, (255, 255, 255), (50, 240 + space, 300, 100), 1)
        # screen.blit(pygame.draw.rect(self.screen, (255, 255, 255), (50, 0 + space, 300, 100), 1))
        pygame.display.flip()
        pass

    def sound(self):
        self.buttton_sound.play()

    def get_click(self, mouse_pos):
        print(mouse_pos)
        x, y = mouse_pos
        # if  self.survival_mask.collidepoint(x, y):
        #     print('Area clicked.')
        self.sound()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    # pygame.mouse.set_visible(False)
    screen.fill((0, 0, 0))

    x_pos = 0
    v = 500  # пикселей в секунду
    clock = pygame.time.Clock()
    running = True
    exp1 = Menu('menu.jpg', screen, 0, 0, 'sounds\mouse2.wav')
    # exp1.but()
    exp1.background()
    # exp1.load_image('options.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                exp1.get_click(event.pos)
                exp1.sound()
        x_pos += v * clock.tick() / 1000  # v * t в секундах
        pygame.display.flip()

    pygame.quit()
