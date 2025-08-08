import pygame
from core.events.EngineClick import EngineClick
from application.objects.cards.Rune import Card
from core.events.EventFunctionManager import Event
from core.sprites import EngineSpriteGroup

class CardHand(EngineSpriteGroup):
    def __init__(self):
        super().__init__()
        self.__runeHandLimit = 7
        self.__isHidden = False

    def isHidden(self) -> bool:
        return self.__isHidden  

    def setHidden(self, hidden: bool):
        self.__isHidden = hidden

    def addCard(self, rune: Card):
        if len(self) < self.__runeHandLimit:
            self.add(rune)

    def removeCard(self, index: int):
        if 0 <= index < len(self):
            spriteList = list(self.sprites())
            self.remove(spriteList[index])

    def removeCard(self, rune: Card):
        if rune in self:
            self.remove(rune)

    @EngineClick(rect=pygame.Rect(125, 675, 1030, 95), blockWhenDragging=False)
    def onClick(self, *args, **k):
        event: Event = k["event"]
        dragObj = event.getDragObject()
        if dragObj and dragObj.hasCursorSprite() and isinstance(dragObj.getCursorSprite(), Card):
            self.add(dragObj.getCursorSprite())
            dragObj.invalidate()