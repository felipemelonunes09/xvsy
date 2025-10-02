
import pygame
from application.entities.hands.RuneHand import CardHand
from application.scene.LowerDeck import LowerDeck

class TableEntity(pygame.sprite.Group):
    def __init__(self, lowerDeckPosition = (0, 0), cardHandPosition = (0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__cardHand = CardHand(position=cardHandPosition)
        self.__runeDeck = LowerDeck(position=lowerDeckPosition)

        self.add(self.__runeDeck)
        self.add(self.__cardHand)

    def getCardHand(self) -> CardHand:
        return self.__cardHand
    
    def getRuneFrame(self) -> LowerDeck:
        return self.__runeDeck
    