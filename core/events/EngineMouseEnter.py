

from core.events.EngineAction import EngineAction
from core.events.EventFunctionManager import EventFunctionManager


class EngineMouseEnter(EngineAction):
    def __init__(self, *a, **k):
        super().__init__(validator=EngineAction.rectPointValidate, type=EventFunctionManager.EventType.MOUSE_ENTER,  *a, **k)
