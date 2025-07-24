
from collections.abc import Callable
from core.Engine import Engine
import pygame

class EngineClick:
    
    EngineEventFunctionAttr             = "__EngineEventFunction__"
    EngineEventFunctionBindAttr         = "__EngineEventFunctionBind__"
    EngineEventBlockWhenDraggingAttr    = "__EngineEventBlockWhenDragging__"

    def __init__(self, rect: pygame.Rect, blockWhenDragging = True):
        print("    " + str(blockWhenDragging))
        self.__rect = rect
        self.__blockWhenDragging = blockWhenDragging

    def __call__(self, function: Callable, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        
        def register(ref: object):
            Engine.eventFunctionBind(wrapper.__hash__(), ref)
                
        wrapper.__EngineEventFunction__ = True
        wrapper.__EngineEventFunctionBind__ = register
        wrapper.__EngineEventBlockWhenDragging__ = self.__blockWhenDragging
        
        Engine.eventFunctionRegister(type="click", f=wrapper, rect=self.__rect)
        return wrapper