
import pygame
from application.objects.cards.Rune import RuneCard
from application.scene.RuneFrame import RuneFrame
from config.Configuration import Configuration


class LowerDeck(pygame.sprite.Group):
    
    def __init__(self, position: tuple[int, int], *a, **k):
        super().__init__(*a, **k)
        self.runesFrame = [RuneFrame(position=[position[0] + index*Configuration.game_style_frame_offset, position[1]]) for index in range(7)]
        self.add(*self.runesFrame)
        self.__hasDroppedRune = False

    def hasDroppedRune(self) -> bool:
        return self.__hasDroppedRune
    
    def put(self, index: int, runeCard: RuneCard):
        self.runesFrame[index].setCard(runeCard)

    def isFull(self) -> bool:
        for rf in self.runesFrame:
            if not rf.hasCard():
                return False
        return True

