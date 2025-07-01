import pygame

from application.objects.cards.Card import PlainCard
from core.EngineClick import EngineClick

class RuneDeck(pygame.sprite.Group):
    def __init__(self, position: tuple[int, int] = (0, 0), *a, **k):
        super().__init__(*a, **k)
        for index in range(5):
            self.add(PlainCard(position=(position[0] + index * 5, position[1]), scale=(100, 100)))

    @EngineClick(rect=pygame.Rect(65, 300, 95, 95))
    def onClick(self, event: pygame.event.Event):
        pass