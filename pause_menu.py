from datetime import datetime

import pygame
import os
import sys
from load_image import load_image

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
                all_sprites_pause_menu.remove(back_to_game_btn)
                all_sprites_pause_menu.remove(main_menu_btn)
                all_sprites_pause_menu.remove(restart_level_btn)
                all_sprites_pause_menu.remove(pause_menu)

                all_buttons_pause_menu.remove(back_to_game_btn)
                all_buttons_pause_menu.remove(main_menu_btn)
                all_buttons_pause_menu.remove(restart_level_btn)
                all_buttons_pause_menu.remove(pause_menu)

                screen.fill((0, 0, 0))
                return 1
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


def terminate():
    pygame.quit()
    sys.exit()


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)
# pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))

all_buttons_pause_menu = pygame.sprite.Group()
all_sprites_pause_menu = pygame.sprite.Group()

# окно паузы
pause_menu = Pause_Menu_bg(350, 0, 'pause_menu.png', all_sprites_pause_menu)

# кнопки паузы
back_to_game_btn = Button(350, 0, 'back_to_game_pause_menu.png', True, 'back_to_game', all_buttons_pause_menu,
                          all_sprites_pause_menu)
main_menu_btn = Button(350, 0, 'main_menu_pause_menu.png', True, 'main_menu', all_buttons_pause_menu,
                       all_sprites_pause_menu)
restart_level_btn = Button(350, 0, 'restart_level_pause_menu.png', True, 'restart_level', all_buttons_pause_menu,
                           all_sprites_pause_menu)


def launch_pause_menu():
    # if __name__ == '__main__':
    # pygame.init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_buttons_pause_menu.update(pygame.mouse.get_pos())
            all_sprites_pause_menu.draw(screen)
        pygame.display.flip()
    return 1
    # pygame.quit()


# launch_pause_menu()
