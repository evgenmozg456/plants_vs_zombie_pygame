import pygame
import os
import sys
from load_image import load_image


# окно для изображения проигрыша
class EndScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = load_image('image_end_game', image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # воспроизведение звука
    def sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()


def terminate():
    pygame.quit()
    sys.exit()


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

end_screen_sprite = pygame.sprite.Group()

# окно конца игры
pause_menu = EndScreen(0, 0, 'end_screen.png', end_screen_sprite)


def launch_end_screen():
    # if __name__ == '__main__':
    pygame.init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            end_screen_sprite.draw(screen)
        pygame.display.flip()
    pygame.quit()

# launch_end_screen()
