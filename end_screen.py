import pygame

from Menu import terminate
from load_image import load_image
from Board import kill_zombie


# окно для изображения проигрыша
class EndScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (
            width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # воспроизведение звука
    def sound_defeat(self):
        self.sound_menu = pygame.mixer.music
        self.sound_menu.load('sounds\defeat.wav')
        self.sound_menu.play()


size = width, height = 1900, 800
screen = pygame.display.set_mode(size)

end_screen_sprite = pygame.sprite.Group()

# окно конца игры
lastScreen = EndScreen(0, 0, 'image_end_game/end_screen.png', end_screen_sprite)


def launch_end_screen():
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 100)

    with open('Score_zombies.txt', 'r') as file:
        score = file.read()

    num = font.render(f'{score}', True, (100, 255, 100))


    running = True
    lastScreen.sound_defeat()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            #     по нажатие в любую часть окна переходишь в главное меню
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                lastScreen.sound_menu.pause()
                return 1
            end_screen_sprite.draw(screen)
            screen.blit(num, (1000, 700))
        pygame.display.flip()
    pygame.quit()



if __name__ == '__main__':
    launch_end_screen()
