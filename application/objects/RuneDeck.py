import pygame
import random 

from config.Configuration import Configuration
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
            self.add(PlainCard(position=(position[0] + index * 5, position[1]), scale=Configuration.card_scale))

    @EngineClick(rect=pygame.Rect(65, 300, 95, 95))
    def onClick(self, *args, **k):
        self.__clicked = True

    def next(self) -> RuneCard:
        rtype = random.choice(self.__possibleRunes)
        return RuneCard(rtype, scale=Configuration.card_scale)

    ## maybe this shoud be in a separate class to be reused
    def isClicked(self) -> bool:
        return self.__clicked
    
    ## maybe this shoud be in a separate class to be reused
    def isClikedAndConsume(self) -> bool:
        if self.__clicked:
            self.__clicked = not self.__clicked
            return True
        return self.__clicked
    