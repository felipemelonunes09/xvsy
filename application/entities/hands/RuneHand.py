import pygame

from application.objects.cards.Rune import RuneCard

class RuneHand(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.__runeHandLimit = 7
        self.__isHidden = False

    def isHidden(self) -> bool:
        return self.__isHidden  

    def setHidden(self, hidden: bool):
        self.__isHidden = hidden

    def addRune(self, rune: RuneCard):
        if len(self) < self.__runeHandLimit:
            self.add(rune)

    def removeRune(self, index: int):
        if 0 <= index < len(self):
            spriteList = list(self.sprites())
            self.remove(spriteList[index])

    def removeRune(self, rune: RuneCard):
        if rune in self:
            self.remove(rune)