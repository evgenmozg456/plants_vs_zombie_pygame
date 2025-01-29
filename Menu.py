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
    def __init__(self, x, y, image, con, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.con = con  # Состояние кнопки
        self.but_name = but_name
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask) and self.con:
            print("OK")
            self.sound('sounds\mouse2.wav')
            if self.but_name == 'exit':
                # return 0
                terminate()
            elif self.but_name == 'survival':
                return 3
            elif self.but_name == 'option':
                # survival_btn.kill()
                # options_btn.kill()
                # quit_btn.kill()
                # self.kill_sprite(survival_btn)
                # self.kill_sprite(options_btn)
                # self.kill_sprite(quit_btn)

                all_buttons.remove(survival_btn)
                all_buttons.remove(options_btn)
                all_buttons.remove(quit_btn)

                screen.fill((0, 0, 0))

                all_sprites.add(option_menu)
                all_sprites.add(options_ok_btn)
                all_buttons.add(options_ok_btn)

            elif self.but_name == 'option_ok':
                screen.fill((0, 0, 0))
                self.kill_sprite(option_menu)
                self.kill_sprite(options_ok_btn)

                all_buttons.add(survival_btn)
                all_buttons.add(options_btn)
                all_buttons.add(quit_btn)

    def kill_sprite(self, name):
        name.kill()

    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()

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




size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


all_buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
survival_btn = Button(0, 0, 'survival_button3.png', True, 'survival', all_buttons, all_sprites)
quit_btn = Button(0, 0, 'quit_but1.png', True, 'exit', all_buttons, all_sprites)
options_btn = Button(0, 0, 'options_but1.png', True, 'option', all_buttons, all_sprites)
menu = Button(0, 0, 'menu.jpg', False, '', all_buttons, all_sprites)
        # меню настроек
option_menu = Options(100, 0, 'options_menu.png')
options_ok_btn = Button(0, 0, 'option_ok_btn2.png', True, 'option_ok')

back = -1



def launch_menu():
    # убрал проверку вызова
    # if __name__ == '__main__':

    pygame.init()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                z = all_buttons.update(pygame.mouse.get_pos())
                print(z)
                if z == 3:
                    running = False
                    return 3
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    print(back)
    # return back

xx = launch_menu()
