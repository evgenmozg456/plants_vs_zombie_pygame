import pygame
from Plants import Plants

class Board(pygame.sprite.Sprite):
    # создание поля
    def __init__(self,size,  width, height, image_path, *groups):
        super().__init__(*groups)
        self.font = pygame.font.Font(None, 50)


        self.width = width
        self.height = height

        image = pygame.image.load(image_path).convert_alpha()

        self.image_pole = pygame.transform.scale(image, size)

        self.rect = self.image_pole.get_rect()

        self.all_sprites_plants = pygame.sprite.Group()
        self.menu_sprites = pygame.sprite.Group()

        self.board = [[0] * width for _ in range(height)]
        self.sprites_menu = ['cards/podsolnux_card.jpg', 'cards/gorox_card.jpg', 'cards/potatomine_card.jpg',
                             'cards/orex_card.jpg', 'cards/cherrybomb_card.jpg', 'cards/lopata.png']  #  спрайты менюшки
        self.sprites_plants = ["plants/sunflower.png", 'plants/gorox_1.jpg',
                               'plants/potatomine.png', "plants/orex.png",
                               "plants/cherry.png"]
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

        self._init_menu()

    def _init_menu(self):
        for i, menu_sprite in enumerate(self.sprites_menu):
            menu = Plants(self.left + 100 * i, 0, menu_sprite)
            self.menu_sprites.add(menu)
    def add_plant(self, plant):
        self.all_sprites_plants.add(plant)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def economica(self, plant=0):
        if plant == 0:
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
            screen.blit(self.shovel_image, (mx - self.shovel_rect.width // 2, my - self.shovel_rect.height // 2))
        else:
            # Если лопата не активна, показываем стандартный курсор
            pygame.mouse.set_visible(True)

        for j in range(self.width):
            for i in range(self.height):
                pos_x = self.left + self.cell_size * j
                pos_y = self.top + self.cell_size * i
                # Рисуем сетку
                pygame.draw.rect(screen, color, (pos_x, pos_y, self.cell_size, self.cell_size), 1)

        # Отображаем спрайты
        self.all_sprites_plants.draw(screen)

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
            if self.board[ay][ax] == 0 and self.sun > 0:  # проверка на растение(т.е если поле уже занято растением ничего не делает)
                if self.economica(self.plants_choice):  # функция проверяет хавтает ли денег
                    self.board[ay][ax] = self.plants_choice

                    if self.plants_choice > 0:
                        x = self.left + ax * self.cell_size
                        y = self.top + ay * self.cell_size
                        plant = Plants(x, y, self.sprites_plants[self.plants_choice - 1])  # Создаем спрайт
                        self.add_plant(plant)
            return ay, ax

        if 0 <= ax <= 5 and 0 <= my // self.cell_size <= (self.height - 1):  # определяется какое растение выбрано
            self.plants_choice = ax + 1  # выбор растени из вверхней панели
            return ax
        else:
            return None





def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Игровое поле')
    pole_image = 'pole.jpg'

    size = 1900, 800
    screen = pygame.display.set_mode(size)

    pygame.mouse.set_visible(True)

    board = Board(size, 10, 6, pole_image)
    running = True
    last_score_time = pygame.time.get_ticks()
    while running:  # самый обычный игровой цикл
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
            board.economica()
            last_score_time = current_time
        pygame.display.flip()
        clock.tick(60)  # счётчик кадрор (fps)



if __name__ == '__main__':
    main()
