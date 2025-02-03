import pygame

from pause_menu import launch_pause_menu
from pause_menu import Button

from Menu import Button
from Menu import launch_menu
from Menu import Options, Background, Button
from Board import Board
from Board import main


def launch_project():
    # инициализация
    pygame.init()
    # size = width, height = 1900, 800
    # screen = pygame.display.set_mode(size)

    # состояние переключателя
    condition = 1
    while condition != 0:
        # открытие главного меню Menu.py
        if condition == 1:
            condition = launch_menu()
        # открытие основной игры Board.py
        elif condition == 2:
            condition = main()
        # открытие меню паузы
        elif condition == 3:
            print('hello word')
            condition = launch_pause_menu()
        # вывод окна проигрыша
        elif condition == 4:
            pass
    pygame.quit()


launch_project()
