# from winreg import SetValueEx
from msvcrt import kbhit

import pygame
import os
import sys


def load_image(name: str):
    fullname = os.path.join('images_main_menu', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, con, but_name,  *group):
        super().__init__(*group)
        self.x = x
        self.con = con # Состояние кнопки
        self.but_name = but_name
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale( self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        # global main_menu, option_menu_triger
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask) and self.con:
            print("OK")
            self.sound('sounds\mouse2.wav')
            if self.but_name == 'exit':
                terminate()
            elif self.but_name == 'survival':
                pass
            elif self.but_name == 'option':
                # menu.kill()
                # all_sprites.remove(survival_btn)
                # all_sprites.remove(options_btn)
                # all_sprites.remove(quit_btn)
                # all_buttons.remove(survival_btn)
                # all_buttons.remove(options_btn)
                # all_buttons.remove(quit_btn)
                # survival_btn.kill()
                # options_btn.kill()
                # quit_btn.kill()
                self.kill_sprite(survival_btn)
                self.kill_sprite(options_btn)
                self.kill_sprite(quit_btn)
                screen.fill((0, 0, 0))

                option_menu = Options(100, 0, 'options_menu.png', all_buttons, all_sprites)
                options_ok_btn = Button(0, 0, 'option_ok_btn2.png', True, 'option_ok', all_buttons, all_sprites)
            elif self.but_name == 'option_ok':
                # option_menu.kill()

                screen.fill((0, 0, 0))

                # self.kill_sprite(option_menu)
    def kill_sprite(self, name):
        name.kill()

    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()

# class Menu(pygame.sprite.Sprite):
#     def __init__(self, name, screen, x, y, sound, colorkey=None):
#         self.name = name
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.changer = True
#         self.buttton_sound = pygame.mixer.Sound(sound)
#         self.back = 0
#
#     def render(self):
#         self.left = width // 4
#
#
#
#     def background(self):
#         # КНОПКА ИГРАТЬ
#
#         # self.sprite.image = pygame.transform.scale(self.sprite.image, (
#         # self.sprite.image.get_width() // 5, self.sprite.image.get_height() // 5))
#         fon = pygame.transform.scale(load_image('menu.jpg'), (
#             width, height))
#         self.survival = pygame.transform.scale(load_image('survival_button3.png'), (
#             width, height))
#         self.quit_but = pygame.transform.scale(load_image('quit_but1.png'), (
#             width, height))
#
#         self.options_but = pygame.transform.scale(load_image('options_but1.png'), (
#             width, height))
#
#         screen.blit(fon, (0, 0))
#         screen.blit(self.options_but, (0, 0))
#         screen.blit(self.quit_but, (0, 0))
#         screen.blit(self.survival, (0, 0))
#         pygame.display.flip()
#
#         # маска для survival
#         self.survival_rect = self.survival.get_rect(center=(width / 2, height / 2))
#         self.survival_mask = pygame.mask.from_surface(self.survival)
#         # маска для quit
#         self.quit_but_rect = self.quit_but.get_rect(center=(width / 2, height / 2))
#         self.quit_but_mask = pygame.mask.from_surface(self.quit_but)
#
#         # маска для options
#         self.options_but_rect = self.options_but.get_rect(center=(width / 2, height / 2))
#         self.options_but_mask = pygame.mask.from_surface(self.options_but)
#
#         # self.sprite.rect = self.sprite.image.get_rect()
#         # screen.fill((200, 200, 200))
#         # self.all_sprites.draw(screen)
#
#     def but(self):
#         # self.area = pygame.Polygon([[640, 200], [1150, 265], [1120, 360], [650, 295]])
#         # pygame.draw.polygon(self.screen, (255, 255, 255), [[640, 200], [1150, 265], [1120, 360], [650, 295]], 1 )
#         # pygame.draw.cirlce(self.screen, (255, 255, 255), (640, 200, 510, 95), 1)
#         # pygame.draw.rect(self.screen, (255, 255, 255), (50, 240 + space, 300, 100), 1)
#         # screen.blit(pygame.draw.rect(self.screen, (255, 255, 255), (50, 0 + space, 300, 100), 1))
#         pygame.display.flip()
#
#     def sound(self, sound):
#
#         sound = pygame.mixer.Sound(sound)
#         sound.play()
#         # self.buttton_sound.play()
#
#     def get_click(self, mouse_pos):
#         self.on_click(mouse_pos)
#         # exp1.sound()
#
#     def on_click(self, mouse_pos):
#         x, y = mouse_pos
#         # проверка что клик был на кнопку survival
#         pos_in_survival_mask = x - exp1.survival_rect.x, y - exp1.survival_rect.y
#         touching_survival = exp1.survival_rect.collidepoint(x, y) and exp1.survival_mask.get_at(pos_in_survival_mask)
#
#         # проверка что клик был на кнопку quit
#         pos_in_quit_but_mask = x - exp1.quit_but_rect.x, y - exp1.quit_but_rect.y
#         touching_quit_but = exp1.quit_but_rect.collidepoint(x, y) and exp1.quit_but_mask.get_at(pos_in_quit_but_mask)
#
#         # проверка что клик был на кнопку options
#         pos_in_options_but_mask = x - exp1.options_but_rect.x, y - exp1.options_but_rect.y
#         touching_options_but = exp1.options_but_rect.collidepoint(x, y) and exp1.options_but_mask.get_at(
#             pos_in_options_but_mask)
#
#         if touching_survival or touching_options_but or touching_quit_but:
#             self.sound()
#         else:
#             pass
#         if touching_quit_but:
#             terminate()
#         if touching_options_but:
#             options = Options()


def terminate():
    pygame.quit()
    sys.exit()


class Options(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


        # screen.fill((0, 0, 0))
        # pygame.display.flip()
        # options_menu = load_image('options_menu.png')

        # screen.blit(options_menu, (100, 0))


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
    # exp1 = Menu('menu.jpg', screen, 0, 0, 'sounds\mouse2.wav')
    # # exp1.but()
    # exp1.background()
    # exp1.load_image('options.png')

    all_buttons = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    # all_option_menu = pygame.sprite.Group()

    survival_btn = Button(0, 0, 'survival_button3.png', True, 'survival', all_buttons, all_sprites)
    quit_btn = Button(0, 0, 'quit_but1.png', True, 'exit', all_buttons, all_sprites)
    options_btn = Button(0, 0, 'options_but1.png', True, 'option',  all_buttons, all_sprites)
    menu = Button(0, 0, 'menu.jpg', False ,'',all_buttons, all_sprites)


    # screen.blit(quit_btn, (0, 0))
    # screen.blit(options_btn, (0, 0))

    # screen.blit(self.options_but, (0, 0))
    # screen.blit(self.quit_but, (0, 0))
    # screen.blit(self.survival, (0, 0))
    # back_ground_menu = Button

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_buttons.update(pygame.mouse.get_pos())
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
