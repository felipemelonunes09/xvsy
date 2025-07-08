
from collections.abc import Callable
from core.Engine import Engine
import pygame

class EngineClick:
    def __init__(self, rect: pygame.Rect):
        self.__rect = rect

    def __call__(self, function: Callable, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        
        def register(ref: object):
            Engine.eventFunctionBind(wrapper.__hash__(), ref)
                
        wrapper.__EngineEventFunction__ = True
        wrapper.__EngineEventFunctionBind__ = register
        
        Engine.eventFunctionRegister(type="click", f=wrapper, rect=self.__rect)
        return wrapper