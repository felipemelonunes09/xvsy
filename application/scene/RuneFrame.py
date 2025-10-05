
import pygame

from application.objects.cards.Rune import RuneCard
from config.Configuration import Configuration
from core.events.EngineClick import EngineClick
from core.events.EventFunctionManager import Event

class RuneFrame(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], *a, **k):
        self.image = pygame.image.load(Configuration.engine_assets_dir / 'images' / 'frame.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        decorator = EngineClick(pygame.Rect(position[0], position[1], 130, 150), blockWhenDragging=False)
        self.onClick = decorator(self.onClick)
        self.expectedRect = pygame.Rect(position[0], position[1], 130, 150)
        self.__card: RuneCard = None

        self.hasDroppedRune = False

        super().__init__(*a, **k)

    def hasCard(self) -> bool:
        return self.__card is not None
    
    def getCard(self) -> RuneCard:
        return self.__card
    
    def setCard(self, runeCard: RuneCard):
        self.__card = runeCard

    def onClick(self, *a, event: Event, **k) -> None:
        dragObj = event.globalState.getDragObject()
        if dragObj and dragObj.hasCursorSprite() and isinstance(dragObj.getCursorSprite(), RuneCard):
            if (self.__card):
                self.__card.kill()
            self.setCard(dragObj.getCursorSprite())
            dragObj.invalidate()
            self.hasDroppedRune = True

    def hasDroppedAndConsume(self) -> bool:
        if self.hasDroppedRune:
            self.hasDroppedRune = False
            return True
        return False    

