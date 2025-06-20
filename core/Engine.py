from __future__ import annotations

from abc import ABC, abstractmethod
from config.Configuration import Configuration
from core.Bootstrap import Bootstrap
from core.loggers import engineInfo, engineLog

import pygame

class Bridge:
    def __init__(self, engine: Engine):
        self.__engine = engine 

    def setBackground(self, surface: pygame.Surface):
        engineLog(f"Setting background image -o {surface}")
        return self.__engine.setBackground(surface)

class Engine:
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

            self.__gameInstance.getSprites().draw(self.__screen)
            print(self.__gameInstance.getSprites())
            

    def setRunning(self, running: bool):
        self.__running = running

    def setBackground(self, surface: pygame.Surface):
        engineLog("Setting background image -resolution " + Configuration.engine_resolution.__str__())
        self.__background = pygame.transform.scale(surface, Configuration.engine_resolution)

    def __handleEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setRunning(False)

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