from abc import ABCMeta
from pathlib import Path
from config.Configuration import Configuration
import pygame

class ICard(metaclass=ABCMeta):
    pass

class Card(pygame.sprite.Sprite, ICard):
    def __init__(self, path: Path, position: tuple[int, int] = None, scale: tuple[int, int] = None, *a, **kwargs):
        super().__init__(*a, **kwargs)
        img         = pygame.image.load(path)
        self.image  = pygame.transform.scale(img, scale) if scale else img
        self.rect   = self.image.get_rect()
        if position:
            self.rect.topleft = position
    
class PlainCard(Card):
    def __init__(self, *a, **kwargs):
        super().__init__(Configuration.engine_assets_dir / 'images' / 'cards' / f'template-card.png', *a, **kwargs)