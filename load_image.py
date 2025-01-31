import os
import sys
import pygame


pygame.init()

#  функции теперь нужно передавать путь и название файла
def load_image(way, name, colorkey=None):
    fullname = os.path.join(way, name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image