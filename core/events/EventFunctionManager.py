
from __future__ import annotations
from collections.abc import Callable
from enum import Enum
import pygame

class Event:
    def __init__(self, type: EventFunctionManager.EventType, globalState: EventFunctionManager.GlobalState, event: pygame.event.Event):
        self.globalState = globalState
        self.__gameEvent = event
        self.__type = type

    def getDragObject(self) -> EventFunctionManager.Drag:
        return self.__dragObject
    
    def getGameEvent(self) -> pygame.event.Event:
        return self.__gameEvent

class EventFunctionManager:

    class EventType(Enum):
        CLICK       = 1
        MOUSE_MOVE  = 2
        MOUSE_ENTER = 3
        MOUSE_LEAVE = 4
        CUSTOM      = 5 

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

    # should enforce the isDragging logic here
    class GlobalState:
        def __init__(self):
            self.__isDragging: bool = False
            self.__dragObject: EventFunctionManager.Drag = None

        def isDragging(self) -> bool:
            if (self.__dragObject):
                return self.__isDragging and self.__dragObject.isValid()
            return self.__isDragging
        
        def setDragging(self, dragging: bool) -> False:
            self.__isDragging = dragging

        def getDragObject(self) -> EventFunctionManager.Drag:
            if self.__dragObject:
                if self.__dragObject.isValid():
                    return self.__dragObject
        
        def setDragObject(self, dragObject: EventFunctionManager.Drag):
            self.__dragObject = dragObject
            
    class Dispatcher:
        @staticmethod
        def route(contactList: list[EventFunctionManager.EventRegister], payload: dict, reroute: Callable):
            for contact in contactList:
                eventRegister: EventFunctionManager.EventRegister = contactList[contact]
                function    = eventRegister.getHandler()
                result      = function.__EngineEventFunctionValidate__(**eventRegister.getPayload(), **payload)
                if result:
                    event = Event(**payload)
                    if (event.globalState.isDragging() and not function.__EngineEventBlockWhenDragging__) or not event.globalState.isDragging():
                        function(eventRegister.getReference(), event=Event(**payload))

                if (eventRegister.getStoredTrigger() == True and result == False and eventRegister.getOnTriggerFall()):
                    reroute(eventRegister.getOnTriggerFall())

                if (eventRegister.getStoredTrigger() == False and result == True and eventRegister.getOnTriggerRise()):
                    reroute(eventRegister.getOnTriggerRise())

                eventRegister.setStoredTrigger(result)

        @staticmethod
        def reroute(contactList: list[EventFunctionManager.EventRegister], payload: dict):
            for contact in contactList:
                eventRegister: EventFunctionManager.EventRegister = contactList[contact]
                function    = eventRegister.getHandler()
                event = Event(**payload)
                if (event.globalState.isDragging() and not function.__EngineEventBlockWhenDragging__) or not event.globalState.isDragging():
                    function(eventRegister.getReference(), event=Event(**payload))


    class EventRegister:
        def __init__(self, handler: Callable, payload: dict, reference: object, onTriggerRise: EventFunctionManager.EventType, onTriggerFall: EventFunctionManager.EventType):
            self.__handler = handler
            self.__reference = reference
            self.__payload = payload
            self.__onTriggerRise = onTriggerRise
            self.__onTriggerFall = onTriggerFall
            self.__storedTrigger = False

        def getOnTriggerRise(self) -> EventFunctionManager.EventType:
            return self.__onTriggerRise
        
        def getOnTriggerFall(self) -> EventFunctionManager.EventType:
            return self.__onTriggerFall

        def getStoredTrigger(self) -> bool:
            return self.__storedTrigger
        
        def setStoredTrigger(self, trigger: bool):
            self.__storedTrigger = trigger

        def setReference(self, reference: object):
            self.__reference = reference

        def getPayload(self) -> dict:
            return self.__payload
        
        def getHandler(self) -> Callable:
            return self.__handler
        
        def getReference(self) -> object:
            return self.__reference
        
    def __init__(self):
        self.globalState    : EventFunctionManager.GlobalState                                                          = EventFunctionManager.GlobalState()
        self.__eventTree    : dict[EventFunctionManager.EventType, dict[int, list[EventFunctionManager.EventRegister]]] = dict()

    def createDrag(self, dragObj: EventFunctionManager.Drag) -> None:
        self.globalState.setDragging(True)
        self.globalState.setDragObject(dragObj)

    def destroyDrag(self) -> None:
        self.globalState.setDragging(False)
        self.globalState.setDragObject(None)

    def getEventsListeners(self, topic: EventFunctionManager.EventType) -> dict[int, list[EventFunctionManager.EventRegister]]:
         return self.__eventTree.get(topic, {})

    def On(self, type: EventFunctionManager.EventType, eventRegister: EventFunctionManager.EventRegister):
        bucket = self.__eventTree.setdefault(type, {})
        bucket[eventRegister.getHandler().__hash__()] = eventRegister 

    def Emit(self, type: EventFunctionManager.EventType, payload: dict = {}):
        ## enforce a global state here
        def reroute(retype: EventFunctionManager.EventType, *a):
           self.Dispatcher.reroute(self.getEventsListeners(retype), payload={
                **payload,
                "type": retype,
                "globalState": self.globalState
            })

        self.Dispatcher.route(self.getEventsListeners(type), payload={
            **payload,
            "type": type,
            "globalState": self.globalState
        },reroute=reroute) 

