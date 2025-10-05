from __future__ import annotations

from types import SimpleNamespace
from typing import Callable, Self
from config.Configuration import Configuration
from core.Bootstrap import Bootstrap
from core.animations.AnimationBase import Animation
from core.events.EventFunctionManager import Event, EventFunctionManager
from core.loggers import engineInfo, engineLog
from abc import ABC, abstractmethod

import pygame

class Bridge:
    def __init__(self, engine: Engine):
        self.__engine = engine 

    def setBackground(self, surface: pygame.Surface):
        engineLog(f"Setting background image -o {surface}")
        return self.__engine.setBackground(surface)
    
    def startDrag(self, payload: object, cursorSprite: pygame.sprite.Sprite):
        engineInfo(f"Starting drag with payload: {payload}")
        return self.__engine.getEventFunctionManager().createDrag(EventFunctionManager.Drag(payload, cursorSprite))
    
    def addAnimation(self, animation: Animation):
        self.__engine.getAnimation().append(animation)

class Engine:
    eventFunctionManager: EventFunctionManager = EventFunctionManager()
    def __init__(self, context: Bootstrap.Context, gameInstance: GameInstance):

        self.__context          :Bootstrap.Context       = context
        self.__screen           :pygame.Surface          = context.screen()
        self.__background       :pygame.Surface          = None
        self.__clock            :pygame.time.Clock       = context.clock()
        self.__gameInstance     :GameInstance            = gameInstance
        self.__bridge           :Bridge                  = Bridge(self)
        self.__animations       :list[Animation]         = []

        self.setRunning(False)

    def run(self):
        self.setRunning(True)
        self.__gameInstance.setBridge(self.__bridge)
        self.__gameInstance.setup()

        engineLog("Game instance setup complete.")
        engineInfo("\tStarting game loop...")

        while self.__running:

            self.__handleEventLoop()
            self.__handleAnimationLoop()
            self.__gameInstance.update()
            self.__gameInstance.getSprites().update()
            self.__context.flipOver()

            if self.__background:
                self.__screen.blit(self.__background, (0, 0))

            # consider moving this to another function or class
            if self.eventFunctionManager.globalState.isDragging():
                pos         = pygame.mouse.get_pos()
                dragObject  = self.eventFunctionManager.globalState.getDragObject()
                if dragObject.hasCursorSprite():
                    cursor = dragObject.getCursorSprite()
                    cursor.rect.center = pos

            if Configuration.debug:
                clickEvents = Engine.eventFunctionManager.getEventsListeners(EventFunctionManager.EventType.CLICK)
                for key in clickEvents:
                    pygame.draw.rect(self.__screen, Configuration.debug_area_color, clickEvents[key].getPayload().get("rect"), width=2)
                clickEvents = Engine.eventFunctionManager.getEventsListeners(EventFunctionManager.EventType.MOUSE_MOVE)
                for key in clickEvents:
                    pygame.draw.rect(self.__screen, "yellow", clickEvents[key].getPayload().get("rect"), width=2)
                
            self.__gameInstance.getSprites().draw(self.__screen)

    def getAnimation(self) -> list[Animation]:            
        return self.__animations

    def setRunning(self, running: bool):
        self.__running = running

    def setBackground(self, surface: pygame.Surface):
        engineLog("Setting background image -resolution " + Configuration.engine_resolution.__str__())
        self.__background = pygame.transform.scale(surface, Configuration.engine_resolution)

    def getEventFunctionManager(self) -> EventFunctionManager:
        return self.eventFunctionManager

    def __handleEventLoop(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.setRunning(False)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.eventFunctionManager.Emit(EventFunctionManager.EventType.CLICK, {"event": e})
            if e.type == pygame.MOUSEMOTION:
                self.eventFunctionManager.Emit(EventFunctionManager.EventType.MOUSE_MOVE, { "event": SimpleNamespace(pos=pygame.mouse.get_pos())})

    def __handleAnimationLoop(self):
        print(self.__animations)
        for anim in self.__animations:
            anim.update(self.__context.delta())
            if anim.isFinished():
                self.__animations.remove(anim)
    
    @staticmethod
    def registerEventCallback(type: EventFunctionManager.EventType, eventRegister: EventFunctionManager.EventRegister):
        Engine.eventFunctionManager.On(type, eventRegister)

    @staticmethod
    def bindEventObject(type: EventFunctionManager.EventType, function: Callable, ref: object):
        engineInfo(f"Binding event function with fhash {function.__hash__} and reference {ref}")
        Engine.eventFunctionManager.getEventsListeners(type)[function.__hash__()].setReference(ref)


class IGameInstance(ABC):
    
    @abstractmethod
    def getSprites(self) -> pygame.sprite.Group:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def addSprite(self, sprite: pygame.sprite.Sprite) -> Self:
        pass

    @abstractmethod
    def addAnimation(self, animation: Animation) -> Self:
        pass
    
    @abstractmethod
    def setup(self):
        pass
    
class GameInstance(IGameInstance):
    def setBridge(self, bridge: Bridge):
        self.engine = bridge
        self.__allSprites = pygame.sprite.Group()

    def getEngine(self) -> Bridge:
        return self.engine
    
    def getSprites(self) -> pygame.sprite.Group:
        return self.__allSprites
    
    def addSprite(self, sprite: pygame.sprite.Sprite | pygame.sprite.Group) -> Self:
        self.getSprites().add(sprite)
        return self
    
    def addAnimation(self, animation: Animation) -> Self:
        self.getEngine().addAnimation(animation)
        return self
