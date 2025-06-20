
import pygame
from application.objects.cards.Rune import IRune

class TableEntity(pygame.sprite.Group):
    def __init__(self):
        self.__runeHand = pygame.sprite.Group()
        self.__runeHandLimit = 7

    def addRune(self, rune: IRune):
        if (len(self.__runeHand) < self.__runeHandLimit):
            self.__runeHand.add(IRune)

    def removeRune(self, index: int):
        spriteList = list(self.__runeHand.sprites())
        self.__runeHand.remove(spriteList[index])

    