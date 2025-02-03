import pygame
import sys
from load_image import load_image


# класс фона главного меню
class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        # вывод изображения на задний фон
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()


# класс кнопок
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.but_name = but_name  # имя кнопки
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        # проверка клика по кнопке
        global running
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask):
            self.mouseClick('sounds\mouse2.wav')
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

                all_sprites.add(option_menu)
                all_sprites.add(options_ok_btn)
                all_buttons.add(options_ok_btn)
            #  Добавление кнопок меню и закрытие настроек
            elif self.but_name == 'option_ok':
                all_sprites.remove(option_menu)
                all_sprites.remove(options_ok_btn)
                all_buttons.remove(options_ok_btn)

                all_buttons.add(survival_btn)
                all_buttons.add(options_btn)
                all_buttons.add(quit_btn)

    # воспроизводство звука клика
    def mouseClick(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


# класс меню настроек
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


# выход из программы
def terminate():
    pygame.quit()
    sys.exit()


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)

# группы спройтов
all_buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# кнопки
survival_btn = Button(0, 0, 'images_main_menu/survival_button.png', 'survival', all_buttons, all_sprites)
quit_btn = Button(0, 0, 'images_main_menu/quit_but.png', 'exit', all_buttons, all_sprites)
options_btn = Button(0, 0, 'images_main_menu/options_but.png', 'option', all_buttons, all_sprites)

# задний фон
menu = Background(0, 0, 'images_main_menu/menu.jpg', all_sprites)

# меню настроек
option_menu = Options(100, 0, 'images_main_menu/options_menu.png')
options_ok_btn = Button(0, 0, 'images_main_menu/option_ok_btn.png', 'option_ok')

running = True


def launch_menu():
    global running
    # фоновый звук главного меню
    sound_menu = pygame.mixer.Sound('sounds\menu_sound_back.wav')
    sound_menu.play(loops=-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_buttons.update(pygame.mouse.get_pos())

            all_sprites.draw(screen)
        pygame.display.flip()

    sound_menu.set_volume(0)
    # вызов основной игры Board.py

    return 2


if __name__ == '__main__':
    launch_menu()
