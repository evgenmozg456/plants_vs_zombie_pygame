import pygame
from load_image import load_image


# вывод изображения меню паузы
class PauseMenuBg(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            int(width // 1.5), height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# класс кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, but_name, *group):
        super().__init__(*group)
        self.x = x
        self.but_name = but_name
        self.y = y
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            int(width // 1.5), height))
        # создание масок
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        # переменные для переключения между окнами в основной игре
        self.back_to_game_con = False
        self.to_main_menu = False
        self.restart_game = False

    def update(self, pos):
        # проверка клика по кнопке
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.rect.collidepoint(*pos) and self.mask.get_at(pos_in_mask):
            self.sound('sounds\mouse2.wav')
            # закрытие меню
            if self.but_name == 'back_to_game':
                all_sprites_pause_menu.remove(back_to_game_btn)
                all_sprites_pause_menu.remove(main_menu_btn)
                all_sprites_pause_menu.remove(restart_level_btn)
                all_sprites_pause_menu.remove(pause_menu)

                all_buttons_pause_menu.remove(back_to_game_btn)
                all_buttons_pause_menu.remove(main_menu_btn)
                all_buttons_pause_menu.remove(restart_level_btn)
                all_buttons_pause_menu.remove(pause_menu)
                # меняем значение back_to_game_con чтобы убрать спрайты паузы и вернуться в игру
                self.back_to_game_con = True
            # рестарт игры
            elif self.but_name == 'restart_level':
                self.restart_game = True

            # выход в главное меню
            elif self.but_name == 'main_menu':
                all_sprites_pause_menu.remove(pause_menu)
                all_sprites_pause_menu.remove(back_to_game_btn)
                all_sprites_pause_menu.remove(main_menu_btn)
                all_sprites_pause_menu.remove(restart_level_btn)

                all_buttons_pause_menu.remove(back_to_game_btn)
                all_buttons_pause_menu.remove(main_menu_btn)
                all_buttons_pause_menu.remove(restart_level_btn)
                self.to_main_menu = True

    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


# для масштабирования спрайта обозначаем ширину и длину экрана
size = width, height = 1900, 800
# группы спрайтов для меню паузы
all_buttons_pause_menu = pygame.sprite.Group()
all_sprites_pause_menu = pygame.sprite.Group()

# окно паузы
pause_menu = PauseMenuBg(350, 0, 'images_pause_menu/pause_menu.png')

# кнопки паузы
back_to_game_btn = Button(350, 0, 'images_pause_menu/back_to_game_pause_menu.png', 'back_to_game')
main_menu_btn = Button(350, 0, 'images_pause_menu/main_menu_pause_menu.png', 'main_menu')
restart_level_btn = Button(350, 0, 'images_pause_menu/restart_level_pause_menu.png', 'restart_level')
