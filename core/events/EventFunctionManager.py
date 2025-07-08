from collections.abc import Callable
import pygame

class EventFunctionManager:

    FUNCTION    = 0
    RECT        = 1
    REFERENCE   = 2

    def __init__(self):
        self.__click: dict[int, list[Callable, pygame.Rect, object]] = dict()

    def addClickEvent(self, f: Callable, rect: pygame.Rect = None):
        self.__click[f.__hash__()] = [f, rect, None]

    def getClickEvents(self) -> dict[int, list[Callable, pygame.Rect, object]]:
        return self.__click