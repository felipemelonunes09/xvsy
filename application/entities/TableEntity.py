
import pygame
from application.entities.hands.RuneHand import RuneHand

class TableEntity(pygame.sprite.Group):
    def __init__(self):
        self.__runeHand = RuneHand()

    def getRuneHand(self) -> RuneHand:
        return self.__runeHand