import pygame

from collections.abc import Callable
from core.Engine import Engine

from core.events.EngineAction import EngineAction
from core.events.EventFunctionManager import EventFunctionManager

class EngineClick(EngineAction):
    def __init__(self, rect: pygame.Rect, blockWhenDragging: bool = False):
        super().__init__(type=EventFunctionManager.EventType.CLICK, validator=EngineAction.rectPointValidate, rect=rect, blockWhenDragging=blockWhenDragging)
 
 