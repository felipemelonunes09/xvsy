
import pygame

from config.Configuration import Configuration

class RuneFrame(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], *a, **k):
        self.image = pygame.image.load(Configuration.engine_assets_dir / 'images' / 'frame.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        super().__init__(*a, **k)