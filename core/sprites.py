import pygame
from core.loggers import engineInfo, engineLog

class EngineSpriteGroup(pygame.sprite.Group):
    def __init__(self, position: tuple[int, int] = [0, 0], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__position = position
        self.__EngineBind__()

    def getPosition(self, i: int) -> tuple[int, int]:
        if (i < 0 or i > 1):
            return self.__position
        return self.__position[i]   
        
    def __EngineBind__(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr):
                if getattr(attr, "__EngineEventFunction__", False):
                    bind = getattr(attr, "__EngineEventFunctionBind__", None)
                    engineLog(f"Method '{attr_name}' is marked as __EngineEventFunction__")
                    engineInfo(f"\t --> Binding function {bind}")
                    bind(self)
                    print(self.__class__.__name__, attr_name, "is bound to engine events")
                    