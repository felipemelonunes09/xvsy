import pygame
import yaml

from config.Configuration import Configuration
from config import globals
from config.Globalization import Globalization


class Bootstrap:

    ## this class needs to be a singleton to ensure that the context is shared across the application
    class Context:
        def __init__(self, configuration: Configuration):
            self.__screen: pygame.Surface = None
            self.__clock: pygame.time.Clock = None
            self.cg = configuration

        def screen(self) -> pygame.Surface:
            self.__screen = pygame.display.set_mode(self.cg.engine_resolution) if self.__screen is None else self.__screen
            return self.__screen
        
        def clock(self) -> pygame.time.Clock:
            self.__clock = pygame.time.Clock() if self.__clock is None else self.__clock
            return self.__clock
        
        def flipOver(self) -> None:
            pygame.display.flip()
            self.clock().tick(60)  

    def __config__(self) -> Context:
        
        if not globals.WORKING_DIR_PATH.exists() or not globals.DATA_CONFIG_PATH.exists():
            raise Exception(Globalization.WORKING_DIR_NOT_AVAIABLE)
        
        with open(globals.DATA_CONFIG_PATH, 'r', encoding=globals.DATA_CONFIG_ENCODING) as configFile:
            configObject = yaml.safe_load(configFile)
            configuration = Configuration()
            configuration.load(configObject, globals.WORKING_DIR_PATH)

        return Bootstrap.Context(configuration)