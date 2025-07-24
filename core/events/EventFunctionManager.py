
from __future__ import annotations
from collections.abc import Callable
import pygame

class Event:
    def __init__(self, dragObject: EventFunctionManager.Drag, gameEvent: pygame.event.Event):
        self.__dragObject = dragObject
        self.__gameEvent = gameEvent

    def getDragObject(self) -> EventFunctionManager.Drag:
        return self.__dragObject
    
    def getGameEvent(self) -> pygame.event.Event:
        return self.__gameEvent

class EventFunctionManager:
    class Drag:
        def __init__(self, payload: object = None, cursorSprite: pygame.sprite.Sprite = None):
            self.__payload: object = payload
            self.__cursorSprite: pygame.sprite.Sprite = cursorSprite
            self.__isValid = True

        def getPayload(self) -> object:
            return self.__payload
        
        def getCursorSprite(self) -> pygame.sprite.Sprite:
            return self.__cursorSprite
        
        def hasCursorSprite(self) -> bool:
            if self.__cursorSprite:
                return True
            return False
        
        def invalidate(self) -> None:
            self.__isValid = False

        def isValid(self) -> bool:
            return self.__isValid

    class GlobalState:
        def __init__(self):
            self.__isDragging: bool = False
            self.__dragObject: EventFunctionManager.Drag = None

        def isDragging(self) -> bool:
            if (self.__dragObject):
                return self.__isDragging and self.__dragObject.isValid()
            return self.__isDragging
        
        def setDragging(self, dragging: bool):
            self.__isDragging = dragging

        def getDragObject(self) -> EventFunctionManager.Drag:
            if self.__dragObject:
                if self.__dragObject.isValid():
                    return self.__dragObject
        
        def setDragObject(self, dragObject: EventFunctionManager.Drag):
            self.__dragObject = dragObject

    FUNCTION    = 0
    RECT        = 1
    REFERENCE   = 2

    def __init__(self):
        self.__click        : dict[int, list[Callable, pygame.Rect, object]] = dict()
        self.globalState    : EventFunctionManager.GlobalState               = EventFunctionManager.GlobalState()

    def addClickEvent(self, f: Callable, rect: pygame.Rect = None):
        self.__click[f.__hash__()] = [f, rect, None]

    def getClickEvents(self) -> dict[int, list[Callable, pygame.Rect, object]]:
        return self.__click
    
    def createDrag(self, dragObj: EventFunctionManager.Drag) -> None:
        self.globalState.setDragging(True)
        self.globalState.setDragObject(dragObj)

    def destroyDrag(self) -> None:
        self.globalState.setDragging(False)
        self.globalState.setDragObject(None)