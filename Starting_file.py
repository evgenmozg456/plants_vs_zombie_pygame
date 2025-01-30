import pygame

from pause_menu import launch_pause_menu
from pause_menu import Button

from Menu import Button
from Menu import launch_menu
from Menu import Options, Background, Button
from Board import Board
from Board import main

def launch_project():
    pygame.init()
    size = width, height = 1900, 800
    screen = pygame.display.set_mode(size)

    # состояние переключателя
    condition = 1
    while condition != 0:
        if condition == 1:
            # pass
            condition = launch_menu()

        elif condition == 3:
            print('hello word')
            condition = launch_pause_menu()
            print(1232132133)
        elif condition == 4:
            condition = main()
    pygame.quit()

launch_project()