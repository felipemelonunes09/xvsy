

import pygame
from core.events.EngineAction import EngineAction
from core.events.EventFunctionManager import EventFunctionManager


class EngineMouseLeave(EngineAction):
    def __init__(self, rect: pygame.Rect, blockWhenDragging: bool = True):
        super().__init__(validator=EngineAction.rectPointValidate, type=EventFunctionManager.EventType.MOUSE_LEAVE, blockWhenDragging=blockWhenDragging, rect=rect)