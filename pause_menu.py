from datetime import datetime

import pygame
import os
import sys
from load_image import load_image


# вывод изображения меню паузы
class Pause_Menu_bg(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image('images_pause_menu', image)
        self.image = pygame.transform.scale(self.image, (
            int(width // 1.5), height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# класс кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, con, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.con = con  # Состояние кнопки
        self.but_name = but_name
        self.y = y
        self.image = load_image('images_pause_menu', image)
        self.image = pygame.transform.scale(self.image, (
            int(width // 1.5), height))
        # создание масок
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

        self.back_to_game_con = False
        self.to_main_menu = False

    def update(self, pos):
        # проверка клика по кнопке
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask) and self.con:
            self.sound('sounds\mouse2.wav')
            # закрытие меню
            if self.but_name == 'back_to_game':
                print('back_to_game')
                all_sprites_pause_menu.remove(back_to_game_btn)
                all_sprites_pause_menu.remove(main_menu_btn)
                all_sprites_pause_menu.remove(restart_level_btn)
                all_sprites_pause_menu.remove(pause_menu)

                all_buttons_pause_menu.remove(back_to_game_btn)
                all_buttons_pause_menu.remove(main_menu_btn)
                all_buttons_pause_menu.remove(restart_level_btn)
                all_buttons_pause_menu.remove(pause_menu)
                self.back_to_game_con = True

                screen.fill((0, 0, 0))
                # return 1
            # рестарт игры
            elif self.but_name == 'restart_level':
                print('restart_level')
            # выход в главное меню
            elif self.but_name == 'main_menu':
                self.to_main_menu = True
                print('main_menu')

    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


def terminate():
    pygame.quit()
    sys.exit()



size = width, height = 1900, 800
screen = pygame.display.set_mode(size)

all_buttons_pause_menu = pygame.sprite.Group()
all_sprites_pause_menu = pygame.sprite.Group()

# окно паузы
pause_menu = Pause_Menu_bg(350, 0, 'pause_menu.png')

# кнопки паузы
back_to_game_btn = Button(350, 0, 'back_to_game_pause_menu.png', True, 'back_to_game')
main_menu_btn = Button(350, 0, 'main_menu_pause_menu.png', True, 'main_menu')
restart_level_btn = Button(350, 0, 'restart_level_pause_menu.png', True, 'restart_level')



# def launch_pause_menu():
#     # if __name__ == '__main__':
#     pygame.init()
#     running = True
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 terminate()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 all_buttons_pause_menu.update(pygame.mouse.get_pos())
#             all_sprites_pause_menu.draw(screen)
#         pygame.display.flip()
#     return 1
#     pygame.quit()
#
#
# launch_pause_menu()
