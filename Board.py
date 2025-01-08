import pygame
from pygame import font
from load_image import load_image
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


        self.board = [[0] * width for _ in range(height)]
        self.color_plants = ['black', 'yellow', 'green', 'brown', 'burlywood1', 'red', 'grey']  # в будущем тут будут спрайты растений
        self.menu = [i for i in range(len(self.color_plants))]

        self.plants_choice = 0  # показывает какое растение выбрали
        self.sun = 1000  # начальное кол-во солнышек

        # значения по умолчанию
        self.left = 350
        self.top = 150
        self.cell_size = 100

    def add_plant(self, plant):
        self.all_sprites_plants.add(plant)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def economica(self, plant=0):
        if plant == 0:  # пассивынй доход
            self.sun += 25
        else:
            # идёт проверка нужно ли ставить растения
            if self.sun > 0:  # можно улучшить, но мне впадлу, зато работает
                if self.plants_choice == 1:
                    if self.sun - 50 >= 0:
                        self.sun -= 50
                        return True
                if self.plants_choice == 2:
                    if self.sun - 100 >= 0:
                        self.sun -= 100
                        return True
                if self.plants_choice == 3:
                    if self.sun - 25 >= 0:
                        self.sun -= 25
                        return True
                if self.plants_choice == 4:
                    if self.sun - 50 >= 0:
                        self.sun -= 50
                        return True
                if self.plants_choice == 5:
                    if self.sun - 150 >= 0:
                        self.sun -= 150
                        return True
            else:
                # если не хватает денег(солнышек)
                return False

    def render(self, screen):
        color = (255, 255, 255)
        screen.blit(self.image_pole, (0, 0))

        sun = self.font.render(f"{self.sun}", True, (255, 255, 255))
        name_sun = self.font.render("sun", True, (255, 255, 255))

        screen.blit(sun, (100, 50))
        screen.blit(name_sun, (110, 0))

        for i in range(6):
            pos_x = self.left + self.cell_size * i
            pygame.draw.rect(screen, self.color_plants[i + 1], (pos_x, 0, self.cell_size, self.cell_size), 0)

        for j in range(self.width):
            for i in range(self.height):
                pos_x = self.left + self.cell_size * j
                pos_y = self.top + self.cell_size * i

                # Рисуем сетку
                pygame.draw.rect(screen, color, (pos_x, pos_y, self.cell_size, self.cell_size), 1)

        # Отображаем спрайты
        self.all_sprites_plants.draw(screen)

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

                    x = self.left + ax * self.cell_size
                    y = self.top + ay * self.cell_size

                    if self.plants_choice == 1:
                        gorox = Plants(x, y, "plants\sunflower.png")  # Создаем спрайт "подсолнуха"
                        self.add_plant(gorox)

                    if self.plants_choice == 2:
                        gorox = Plants(x, y, "plants\gorox_1.jpg")  # Создаем спрайт "гороха"
                        self.add_plant(gorox)  # Добавляем его в группу спрайтов

                    if self.plants_choice == 3:
                        gorox = Plants(x, y, "plants\potatomine.png")  # Создаем спрайт "подсолнуха"
                        self.add_plant(gorox)

                    if self.plants_choice == 4:
                        gorox = Plants(x, y, "plants\orex.png")  # Создаем спрайт "подсолнуха"
                        self.add_plant(gorox)
                    if self.plants_choice == 5:
                        gorox = Plants(x, y, "plants\cherry.png")  # Создаем спрайт "подсолнуха"
                        self.add_plant(gorox)

            return ay, ax

        if 0 <= ax <= 4 and 0 <= my // self.cell_size <= (self.height - 1):  # определяется какое растение выбрано
            self.plants_choice = ax + 1  # выбор растени из вверхней панели
            return ax

        else:
            return None





def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Игровое поле')
    pole_image = 'pole.jpg'
    gorox_image = 'gorox_1.jpg'

    size = 1900, 800
    screen = pygame.display.set_mode(size)

    board = Board(size, 10, 6, pole_image)
    running = True
    last_score_time = pygame.time.get_ticks()
    while running:  # самый обычный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 - означает левую кнопку мыши
                board.get_click(event.pos)
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
