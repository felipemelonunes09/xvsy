
from collections.abc import Callable
from core.Engine import Engine
import pygame

class EngineClick:
    def __init__(self, rect: pygame.Rect):
        self.__rect = rect

    def __call__(self, function: Callable, *args, **kwargs):
        Engine.register(type="click", f=function, rect=self.__rect)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper