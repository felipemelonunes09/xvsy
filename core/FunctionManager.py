from collections.abc import Callable
import pygame

class FunctionManager:
    def __init__(self):
        self.__click: list[tuple[Callable, pygame.Rect]] = list()

    def addClickEvent(self, f: Callable, rect: pygame.Rect = None):
        self.__click.append((f, rect))

    def getClickEvents(self) -> list[tuple[Callable, pygame.Rect]]:
        return self.__click