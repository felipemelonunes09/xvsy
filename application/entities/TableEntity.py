
import pygame
from application.entities.hands.RuneHand import RuneHand
from application.scene.LowerDeck import LowerDeck

class TableEntity(pygame.sprite.Group):
    def __init__(self, lowerDeckPosition = (0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__runeHand = RuneHand()
        self.__runeDeck = LowerDeck(position=lowerDeckPosition)

        self.add(self.__runeDeck)

    def getRuneHand(self) -> RuneHand:
        return self.__runeHand
    
    def getRuneFrame(self) -> LowerDeck:
        return self.__runeDeck