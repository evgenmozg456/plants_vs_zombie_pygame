from datetime import datetime

import pygame
import os
import sys


def load_image(name: str):
    fullname = os.path.join('images_pause_menu', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, con, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.con = con  # Состояние кнопки
        self.but_name = but_name
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            int(width // 1.5), height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self, pos):
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask) and self.con:
            self.sound('sounds\mouse2.wav')
            if self.but_name == 'back_to_game':
                print('back_to_game')
                all_sprites.remove(back_to_game_btn)
                all_sprites.remove(main_menu_btn)
                all_sprites.remove(restart_level_btn)
                all_sprites.remove(pause_menu)

                all_buttons.remove(back_to_game_btn)
                all_buttons.remove(main_menu_btn)
                all_buttons.remove(restart_level_btn)
                all_buttons.remove(pause_menu)
                screen.fill((0, 0, 0))
            elif self.but_name == 'restart_level':
                print('restart_level')
                # pygame.time.wait(5000)
            elif self.but_name == 'main_menu':
                print('main_menu')

    def kill_sprite(self, name):
        name.kill()

    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


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


def terminate():
    pygame.quit()
    sys.exit()


def pause_menu_fun():
    pass


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)
# pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))

all_buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# all_option_menu = pygame.sprite.Group()

back_to_game_btn = Button(350, 0, 'back_to_game_pause_menu.png', True, 'back_to_game', all_buttons, all_sprites)
main_menu_btn = Button(350, 0, 'main_menu_pause_menu.png', True, 'main_menu', all_buttons, all_sprites)
restart_level_btn = Button(350, 0, 'restart_level_pause_menu.png', True, 'restart_level', all_buttons, all_sprites)
pause_menu = Button(350, 0, 'pause_menu.png', False, '', all_buttons, all_sprites)


def launch_pause_menu():
    # if __name__ == '__main__':
    pygame.init()

    running = True

    # # меню настроек
    # option_menu = Options(100, 0, 'options_menu.png')
    # options_ok_btn = Button(0, 0, 'option_ok_btn2.png', True, 'option_ok')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_buttons.update(pygame.mouse.get_pos())
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
launch_pause_menu()
