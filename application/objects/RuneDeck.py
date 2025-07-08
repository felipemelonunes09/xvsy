import pygame
import random 

from application.objects.cards.Card import PlainCard
from application.objects.cards.Rune import RuneCard
from core.events.EngineClick import EngineClick
from core.sprites import EngineSpriteGroup

class RuneDeck(EngineSpriteGroup):

    def __init__(self, position: tuple[int, int] = (0, 0), *a, **k):
        
        super().__init__(*a, **k)

        self.__clicked = False
        self.__possibleRunes = list(RuneCard.Type)

        for index in range(5):
            self.add(PlainCard(position=(position[0] + index * 5, position[1]), scale=(100, 100)))

    @EngineClick(rect=pygame.Rect(65, 300, 95, 95))
    def onClick(self, event: pygame.event.Event):
        self.__clicked = True

    def next(self) -> RuneCard:
        rtype = random.choice(self.__possibleRunes)
        return RuneCard(rtype)

    ## maybe this shoud be in a separate class to be reused
    def isClicked(self) -> bool:
        return self.__clicked
    