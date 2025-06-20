import pygame

from application.scene.LowerDeck import LowerDeck


class Table(pygame.sprite.Group):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.lowerDecks = [LowerDeck(position=(100, 200)), LowerDeck(position=(100, 500))]
        self.add(*self.lowerDecks)