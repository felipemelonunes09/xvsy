

from core.events.EngineAction import EngineAction
from core.events.EventFunctionManager import EventFunctionManager

class EngineHover(EngineAction):
    def __init__(self, *a, **k):
        super().__init__(validator=EngineAction.rectPointValidate, type=EventFunctionManager.EventType.MOUSE_MOVE, onTriggerRise=EventFunctionManager.EventType.MOUSE_ENTER, onTriggerFall=EventFunctionManager.EventType.MOUSE_LEAVE,**k)