import pygame
from Menu import launch_menu
from Board import main
from end_screen import launch_end_screen


def launch_project():
    # инициализация
    pygame.init()
    # состояние переключателя
    condition = 1
    while condition != 0:
        # открытие главного меню Menu.py
        if condition == 1:
            condition = launch_menu()
        # открытие основной игры Board.py
        elif condition == 2:
            condition = main()
        # вывод окна проигрыша end_screen.py
        elif condition == 3:
            condition = launch_end_screen()
    pygame.quit()


launch_project()
