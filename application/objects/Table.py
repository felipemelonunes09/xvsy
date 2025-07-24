import pygame
from application.scene.LowerDeck import LowerDeck

class Table(pygame.sprite.Group):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        #self.lowerDecks = [LowerDeck(position=(125, 50)), LowerDeck(position=(125, 500))]
        #self.add(*self.lowerDecks)