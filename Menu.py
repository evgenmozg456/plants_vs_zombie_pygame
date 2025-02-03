from msvcrt import kbhit

import pygame
import os
import sys
from load_image import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        # вывод изображения на задний фон
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image('images_main_menu', image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()


class Button(pygame.sprite.Sprite):
    # создание кнопок
    def __init__(self, x, y, image, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.but_name = but_name
        self.y = y
        self.image = load_image('images_main_menu', image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        # проверка клика по кнопке
        global running

        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask):
            self.sound('sounds\mouse2.wav')
            # выход из игры
            if self.but_name == 'exit':
                terminate()
            # если клик по survival, то выходим из цикла и запускаем Board.py
            elif self.but_name == 'survival':
                running = False
            #  удаление кнопок меню и открытие настроек
            elif self.but_name == 'option':
                all_buttons.remove(survival_btn)
                all_buttons.remove(options_btn)
                all_buttons.remove(quit_btn)

                screen.fill((0, 0, 0))

                all_sprites.add(option_menu)
                all_sprites.add(options_ok_btn)
                all_buttons.add(options_ok_btn)
            #  Добавление кнопок меню и закрытие настроек
            elif self.but_name == 'option_ok':
                screen.fill((0, 0, 0))
                all_sprites.remove(option_menu)
                all_sprites.remove(options_ok_btn)
                all_buttons.remove(options_ok_btn)

                all_buttons.add(survival_btn)
                all_buttons.add(options_btn)
                all_buttons.add(quit_btn)

    # воспроизводство звука клика
    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


# выход из программы
def terminate():
    pygame.quit()
    sys.exit()


# класс меню настроек
class Options(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image('images_main_menu', image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
# группы спройтов
all_buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# кнопки
survival_btn = Button(0, 0, 'survival_button3.png', 'survival', all_buttons, all_sprites)
quit_btn = Button(0, 0, 'quit_but1.png', 'exit', all_buttons, all_sprites)
options_btn = Button(0, 0, 'options_but1.png', 'option', all_buttons, all_sprites)

# задний фон
menu = Background(0, 0, 'menu.jpg', all_sprites)

# меню настроек
option_menu = Options(100, 0, 'options_menu.png')
options_ok_btn = Button(0, 0, 'option_ok_btn2.png', 'option_ok')

running = True


def launch_menu():
    global running
    # убрал проверку вызова
    # if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                all_buttons.update(pygame.mouse.get_pos())

            all_sprites.draw(screen)
        pygame.display.flip()

    # вызов основной игры Board.py
    return 2
    # pygame.quit()

# xx = launch_menu()
# print(xx)
