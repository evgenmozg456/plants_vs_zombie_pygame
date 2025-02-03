import pygame
from plants import *
from zombies import *
import random


class Board(pygame.sprite.Sprite):
    # создание поля
    def __init__(self, size, width, height, image_path, *groups):
        super().__init__(*groups)
        self.font = pygame.font.Font(None, 50)

        self.cooldowns = {}

        self.width = width
        self.height = height

        image = pygame.image.load(image_path).convert_alpha()

        self.image_pole = pygame.transform.scale(image, size)

        self.rect = self.image_pole.get_rect()

        self.zombie_y = [100, 200, 300, 400, 500, 600]

        self.all_sprites_plants = pygame.sprite.Group()
        self.all_sprites_zombie = pygame.sprite.Group()
        self.all_sprites_pea = pygame.sprite.Group()
        self.menu_sprites = pygame.sprite.Group()

        self.board = [[0] * width for _ in range(height)]

        self.sprites_menu = ['cards/podsolnux_card.jpg', 'cards/gorox_card.jpg', 'cards/potatomine_card.jpg',
                             'cards/orex_card.jpg', 'cards/cherrybomb_card.jpg', 'cards/lopata.png']  # спрайты менюшки
        self.plant_list_class = [Sunflower, Peashooter, Potatomine, Wallnut, Cherrybomb]

        self.menu = [i for i in range(len(self.sprites_menu))]

        self.plants_choice = 0  # показывает какое растение выбрали
        self.sun = 10000  # начальное кол-во солнышек

        # значения по умолчанию
        self.left = 350
        self.top = 150
        self.cell_size = 100

        self.shovel_image = pygame.image.load("cards/lopata.png").convert_alpha()
        self.shovel_active = False
        self.shovel_rect = pygame.Rect(850, 0, 100, 100)

        self.cooldown = {i + 1: 0 for i in range(len(self.sprites_menu) - 1)}  # словарь для кулдауна всех растений
        self.cooldown_time = 3000  # время перезарядки
        #
        self.lock_image = pygame.image.load('cards/zamok.png').convert_alpha()
        self.lock_image = pygame.transform.scale(self.lock_image, (50, 50))

        self._init_menu()

    def _init_menu(self):
        for i in range(len(self.sprites_menu) - 1):
            class_sprite = self.plant_list_class[i]

            card_plant = class_sprite(self.left + 100 * i, 0, card=True, zombie_group=self.all_sprites_zombie,
                                      pea_group=self.all_sprites_pea)
            self.menu_sprites.add(card_plant)
        card_plant = Shovel(self.left + 100 * (len(self.sprites_menu) - 1), 0, card=True)
        self.menu_sprites.add(card_plant)

    def add_plant(self, plant):
        self.all_sprites_plants.add(plant)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def economica(self, plant=-1):
        if plant == -1:
            self.sun += 25
        else:
            costs = [0, 50, 100, 25, 50, 150]
            if self.sun >= costs[self.plants_choice]:
                self.sun -= costs[self.plants_choice]
                return True
        return False

    def render(self, screen):
        color = (255, 255, 255)
        screen.blit(self.image_pole, (0, 0))

        self.menu_sprites.draw(screen)

        sun = self.font.render(f"{self.sun}", True, (255, 255, 255))
        name_sun = self.font.render("sun", True, (255, 255, 255))
        screen.blit(sun, (100, 50))
        screen.blit(name_sun, (110, 0))

        if self.shovel_active:
            pygame.mouse.set_visible(False)
            mx, my = pygame.mouse.get_pos()
            screen.blit(self.shovel_image, (mx - self.shovel_rect.width // 90, my - self.shovel_rect.height * 2.2))
        else:
            # Если лопата не активна, показываем стандартный курсор
            pygame.mouse.set_visible(True)

        # отрисовка замка
        current_time = pygame.time.get_ticks()
        for i in range(len(self.sprites_menu) - 1):
            if current_time - self.cooldown[i + 1] < self.cooldown_time:
                x = self.left + 100 * i + 25
                y = 25
                screen.blit(self.lock_image, (x, y))

        for j in range(self.width):
            for i in range(self.height):
                pos_x = self.left + self.cell_size * j
                pos_y = self.top + self.cell_size * i
                # Рисуем сетку
                pygame.draw.rect(screen, color, (pos_x, pos_y, self.cell_size, self.cell_size), 1)

        # Отображаем спрайты
        self.all_sprites_plants.draw(screen)
        self.all_sprites_zombie.draw(screen)
        self.all_sprites_pea.draw(screen)

    def render_zombie(self):
        zombie = ZombieFirst(1900, random.choice(self.zombie_y), self.all_sprites_zombie,
                             plants_group=self.all_sprites_plants, pea_group=self.all_sprites_pea)

    def handle_click(self, mouse_pos):
        # print(f"Клик по координатам: {mouse_pos}")
        """Обработка клика мыши."""
        # Если клик по лопате, активируем или деактивируем её
        if self.shovel_rect.collidepoint(mouse_pos):
            self.shovel_active = not self.shovel_active
            print("Клик на лопате!")
            return

        # Если лопата активна
        if self.shovel_active:
            cell = self.get_cell(mouse_pos)
            if cell:
                ay, ax = cell

                # Если в клетке есть растение, удаляем его
                if self.board[ay][ax] != 0:
                    self.board[ay][ax] = 0  # Удаляем растение из логического поля

                    # Удаляем растение из группы спрайтов
                    for plant in self.all_sprites_plants:
                        if plant.rect.collidepoint(mouse_pos):  # Проверяем, совпадает ли клик с растением
                            self.all_sprites_plants.remove(plant)
                            break

            # Деактивируем лопату после использования
            self.shovel_active = False
            return

        # Если лопата не активна, пытаемся поставить растение
        self.get_click(mouse_pos)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell

    def get_cell(self, mouse_pos):
        mx, my = mouse_pos

        ax = (mx - self.left) // self.cell_size
        ay = (my - self.top) // self.cell_size

        if 0 <= ax <= (self.width - 1) and 0 <= ay <= (self.height - 1):  # считывается куда нажал игрок
            if self.board[ay][
                ax] == 0 and self.sun > 0:  # проверка на растение(т.е если поле уже занято растением ничего не делает)
                if self.economica(self.plants_choice):  # функция проверяет хавтает ли денег
                    self.board[ay][ax] = self.plants_choice

                    if self.plants_choice > 0:
                        x = self.left + ax * self.cell_size
                        y = self.top + ay * self.cell_size
                        class_plant = self.plant_list_class[self.plants_choice - 1]
                        plant = class_plant(x, y, zombie_group=self.all_sprites_zombie, pea_group=self.all_sprites_pea)
                        self.all_sprites_plants.add(plant)
                        self.plants_choice = 0
            return ay, ax

        if 0 <= ax < len(self.sprites_menu) - 1 and 0 <= my < self.cell_size:
            current_time = pygame.time.get_ticks()
            if current_time - self.cooldown[ax + 1] >= self.cooldown_time:  # Проверяем перезарядку
                self.plants_choice = ax + 1
                self.cooldown[ax + 1] = current_time  # Записываем время выбора
            return ax
        return None

    def esc(self):
        pass


def main():
    sound_menu = pygame.mixer.music
    sound_menu.load('sounds\zombies_coming.wav')
    sound_menu.play()

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Игровое поле')
    pole_image = 'pole.jpg'

    size = 1900, 800
    screen = pygame.display.set_mode(size)

    # pygame.mouse.set_visible(True)

    board = Board(size, 10, 6, pole_image)
    running = True
    last_score_time = pygame.time.get_ticks()
    board.render_zombie()
    while running:  # самый обычный игровой цикл
        if not pygame.mixer.music.get_busy():
            sound_menu.load('sounds/background_game.wav')
            sound_menu.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 - означает левую кнопку мыши
                board.handle_click(event.pos)

        # if board.shovel_active:
        #     pygame.mouse.set_visible(False)
        # else:
        #     pygame.mouse.set_visible(True)

        screen.fill((0, 0, 0))
        board.render(screen)

        current_time = pygame.time.get_ticks()
        if current_time - last_score_time >= 3000:  # конструкция которая даёт 25 солнышка раз в 3 секунды
            board.economica(-1)
            last_score_time = current_time
        if current_time - last_score_time >= 3000:  # конструкция которая даёт 25 солнышка раз в 3 секунды
            board.render_zombie()
            last_score_time = current_time
        board.all_sprites_zombie.update()
        board.all_sprites_plants.update()
        board.all_sprites_pea.update()
        pygame.display.flip()
        clock.tick(60)  # счётчик кадрор (fps)


if __name__ == '__main__':
    main()
