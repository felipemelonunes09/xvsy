import pygame
from core.loggers import engineInfo, engineLog

class EngineSpriteGroup(pygame.sprite.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__EngineBind__()

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
                    