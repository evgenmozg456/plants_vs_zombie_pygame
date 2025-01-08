import pygame

class Plants(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Масштабируем изображение гороха
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Устанавливаем позицию