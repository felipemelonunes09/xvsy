import pygame
from core.events.EngineMouseLeave import EngineMouseLeave
from core.events.EngineHover import EngineHover
from core.events.EngineClick import EngineClick
from application.objects.cards.Rune import Card
from core.events.EngineMouseEnter import EngineMouseEnter
from core.events.EventFunctionManager import Event
from core.sprites import EngineSpriteGroup

class CardHand(EngineSpriteGroup):

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.__runeHandLimit = 7
        self.__isHidden = False

        decorator = EngineClick(pygame.Rect(self.getPosition(0), self.getPosition(1), 1030, 95), blockWhenDragging=False)
        self.onClick = decorator(self.onClick)

    def isFull(self) -> bool:
        return len(self) >= self.__runeHandLimit

    def isHidden(self) -> bool:
        return self.__isHidden  

    def setHidden(self, hidden: bool):
        self.__isHidden = hidden

    def addCard(self, rune: Card):
        if len(self) < self.__runeHandLimit:
            rune.rect.topleft = (self.getPosition(0) + (len(self) * 40), self.getPosition(1)) 
            self.add(rune)

    def removeCard(self, index: int):
        if 0 <= index < len(self):
            spriteList = list(self.sprites())
            self.remove(spriteList[index])

    def removeCard(self, rune: Card):
        if rune in self:
            self.remove(rune)

    def onClick(self, *args, event: Event, **k):
        dragObj = event.globalState.getDragObject()
        if dragObj and dragObj.hasCursorSprite() and isinstance(dragObj.getCursorSprite(), Card):
            sprite = dragObj.getCursorSprite()
            dragObj.invalidate()
            if (self.isFull()):
                sprite.kill()
            else:
                self.addCard(sprite)

    @EngineHover(rect=pygame.Rect(200, 200, 100, 200), blockWhenDragging=False)
    def onMouseEnter(self, *args, **kwd):
        print("Mouse hover")

    @EngineMouseLeave(rect=pygame.Rect(200, 200, 100, 200), blockWhenDragging=False)
    def onHoverLeave(self, *args, **kwd):
        print("Mouse leave")
    
    def onMouseLeave(self, *args, **kwd):
        pass
