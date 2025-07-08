from __future__ import annotations

from typing import Callable
from config.Configuration import Configuration
from core.Bootstrap import Bootstrap
from core.events.EventFunctionManager import EventFunctionManager
from core.loggers import engineInfo, engineLog
from abc import ABC, abstractmethod

import pygame

class Bridge:
    def __init__(self, engine: Engine):
        self.__engine = engine 

    def setBackground(self, surface: pygame.Surface):
        engineLog(f"Setting background image -o {surface}")
        return self.__engine.setBackground(surface)

class Engine:
    functionManager: EventFunctionManager = EventFunctionManager()
    def __init__(self, context: Bootstrap.Context, gameInstance: GameInstance):

        self.__context          :Bootstrap.Context       = context
        self.__screen           :pygame.Surface          = context.screen()
        self.__background       :pygame.Surface          = None
        self.__clock            :pygame.time.Clock       = context.clock()
        self.__gameInstance     :GameInstance            = gameInstance
        self.__bridge           :Bridge                  = Bridge(self)

        self.setRunning(False)

    def run(self):
        self.setRunning(True)
        self.__gameInstance.setBridge(self.__bridge)
        self.__gameInstance.setup()

        engineLog("Game instance setup complete.")
        engineInfo("\tStarting game loop...")

        while self.__running:
            self.__handleEventLoop()
            self.__gameInstance.update()
            self.__gameInstance.getSprites().update()
            self.__context.flipOver()

            if self.__background:
                self.__screen.blit(self.__background, (0, 0))

            if Configuration.debug:
                clickEvents = Engine.functionManager.getClickEvents()
                for key in clickEvents:
                    pygame.draw.rect(self.__screen, Configuration.debug_area_color, clickEvents[key][EventFunctionManager.RECT], width=2)
            self.__gameInstance.getSprites().draw(self.__screen)            

    def setRunning(self, running: bool):
        self.__running = running

    def setBackground(self, surface: pygame.Surface):
        engineLog("Setting background image -resolution " + Configuration.engine_resolution.__str__())
        self.__background = pygame.transform.scale(surface, Configuration.engine_resolution)

    def __handleEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setRunning(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    engineInfo("\tLeft mouse button clicked at position: " + str(event.pos))
                    clickEvents = Engine.functionManager.getClickEvents()
                    for key in clickEvents:
                        if clickEvents[key][EventFunctionManager.RECT].collidepoint(event.pos):
                            engineInfo(f"\t\tExecuting click event {clickEvents[key][0]} at position {event.pos}")
                            clickEvents[key][EventFunctionManager.FUNCTION](clickEvents[key][EventFunctionManager.REFERENCE], event)

    @staticmethod
    def eventFunctionRegister(type: str, f: Callable, rect: pygame.Rect = None):
        engineLog(f"Registering event handler for type '{type}' with function {f.__name__} and rect {rect}")
        match type:
            case "click": 
                Engine.functionManager.addClickEvent(f, rect)
    @staticmethod
    def eventFunctionBind(fhash: int, reference: object):
        engineInfo(f"Binding event function with fhash {fhash}")
        Engine.functionManager.getClickEvents()[fhash][2] = reference

class IGameInstance(ABC):
    
    @abstractmethod
    def getSprites(self) -> pygame.sprite.Group:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def addSprite(self, sprite: pygame.sprite.Sprite):
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
    
    def addSprite(self, sprite: pygame.sprite.Sprite):
        self.getSprites().add(sprite)