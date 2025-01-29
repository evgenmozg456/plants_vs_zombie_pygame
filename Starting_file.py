import pygame

from pause_menu import launch_pause_menu, pause_menu
from pause_menu import Button
from pause_menu import Options
from  Menu import Button
from Menu import launch_menu
from Menu import Options

pygame.init()
# size = width, height = 1900, 800
# screen = pygame.display.set_mode(size)

# состояние переключателя
con = 1
while con != 0:
    if con == 1:
        con = launch_menu()
    elif con == 3:
        con = launch_pause_menu()

pygame.quit()


