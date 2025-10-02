
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

        self.__card: RuneCard = None

        super().__init__(*a, **k)

    def onClick(self, *a, event: Event, **k) -> None:
        dragObj = event.globalState.getDragObject()
        if dragObj and dragObj.hasCursorSprite() and isinstance(dragObj.getCursorSprite(), RuneCard):
            if (self.__card):
                self.__card.kill()
            self.__card = dragObj.getCursorSprite()
            dragObj.invalidate()

