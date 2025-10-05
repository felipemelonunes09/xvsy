
import pygame
from application.entities.hands.RuneHand import CardHand
from application.scene.LowerDeck import LowerDeck

class TableEntity(pygame.sprite.Group):
    def __init__(self, lowerDeckPosition = (0, 0), cardHandPosition = (0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__cardHand = CardHand(position=cardHandPosition)
        self.__runeDeck = LowerDeck(position=lowerDeckPosition)
        self.__maxMana = 5
        self.__currentMana = 5
        self.__runeCardFromDeckCost = 5

        self.add(self.__runeDeck)
        self.add(self.__cardHand)

    def getCardHand(self) -> CardHand:
        return self.__cardHand
    
    def getLowerDeckSpecs(self) -> list[int | None]:
        list = []
        for runeFrame in self.__runeDeck.runesFrame:
            value = None if not runeFrame.hasCard() else runeFrame.getCard().getValue()
            list.append(value)
                
        return list
    def getRuneFrame(self) -> LowerDeck:
        return self.__runeDeck
    
    # this method shoube by abstract
    def turn(self):
        pass
    
    def setMana(self, mana: int):
        if mana < 0 or mana > self.__maxMana:
            raise ValueError(f"Mana must be between 0 and {self.__maxMana}, got {mana}.")
        self.__currentMana = mana

    def refillMana(self):
        self.__currentMana = self.__maxMana


    def getMana(self) -> int:
        return self.__currentMana

    def getRuneCardFromDeck(self):
        if self.__currentMana < self.__runeCardFromDeckCost:
            raise ValueError(f"Not enough mana to get a rune card from deck. Current mana: {self.__currentMana}, required: {self.__runeCardFromDeckCost}.")
        self.setMana(self.__currentMana - self.__runeCardFromDeckCost)