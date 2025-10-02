
import pygame
from abc import ABCMeta
from core.Engine import Engine
from core.events.EventFunctionManager import EventFunctionManager
from collections.abc import Callable

class EngineAction(metaclass=ABCMeta):
    EngineEventFunctionAttr             = "__EngineEventFunction__"
    EngineEventFunctionBindAttr         = "__EngineEventFunctionBind__"
    EngineEventBlockWhenDraggingAttr    = "__EngineEventBlockWhenDragging__"

    def __init__(self, 
            type: object, 
            validator: Callable, 
            blockWhenDragging=True, 
            rect: pygame.Rect = pygame.Rect(0,0,0,0),
            onTriggerRise: EventFunctionManager.EventType | None = None, 
            onTriggerFall: EventFunctionManager.EventType | None = None
        ):
        self.__blockWhenDragging = blockWhenDragging
        self.__type = type
        self.__validator = validator
        self.__rect = rect
        self.__onTriggerRise = onTriggerRise
        self.__onTriggerFall = onTriggerFall


        
    def __call__(self, function: Callable, *args, **kwds):
        def wrapper(*a, **k):
            return function(*a, **k)
        
        def register(ref: object):
            Engine.bindEventObject(self.__type, wrapper.__hash__(), ref)

        wrapper.__EngineEventFunction__             = True
        wrapper.__EngineEventFunctionBind__         = register
        wrapper.__EngineEventFunctionValidate__     = self.__validator
        wrapper.__EngineEventBlockWhenDragging__    = self.__blockWhenDragging 
        
        # consider in the future here is instatiante EventFunctionManager.EventRegister # its just make sense!!
        

        Engine.registerEventCallback(self.__type, 
            EventFunctionManager.EventRegister(
                reference=None,
                handler=wrapper, 
                onTriggerRise=self.__onTriggerRise, 
                onTriggerFall=self.__onTriggerFall,
                payload={"rect": self.__rect}
            ))
        return wrapper

    @staticmethod
    def rectPointValidate(rect: pygame.Rect, event: pygame.event.Event, **k) -> bool:
        return rect.collidepoint(event.pos)
    
    @staticmethod
    def memoRectPointValidate(rect: pygame.Rect, event: pygame.event.Event, **k) -> bool:
        return rect.collidepoint(event.pos)
    
    def getIsBlockedWhenDragging(self) -> bool:
        return self.__blockWhenDragging
