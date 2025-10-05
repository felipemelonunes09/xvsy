from __future__ import annotations

from enum import Enum
from application.objects.cards.Card import Card
from config.Configuration import Configuration
from abc import ABCMeta, ABC


class IRune(metaclass=ABCMeta):
    pass


class RuneCard(Card, IRune):
    class Type(Enum):
        R_NUMERIC_0             = ("card-numeric-rune-00", 0)
        R_NUMERIC_1             = ("card-numeric-rune-01", 1)
        R_NUMERIC_2             = ("card-numeric-rune-02", 2)
        R_NUMERIC_3             = ("card-numeric-rune-03", 3)
        R_NUMERIC_4             = ("card-numeric-rune-04", 4)
        R_NUMERIC_5             = ("card-numeric-rune-05", 5)
        R_NUMERIC_6             = ("card-numeric-rune-06", 6)
        R_NUMERIC_7             = ("card-numeric-rune-07", 7)
        R_NUMERIC_8             = ("card-numeric-rune-08", 8)
        R_NUMERIC_9             = ("card-numeric-rune-09", 9)
        R_SPECIAL_COMMA         = ("card-special-rune-comma", ",")
        R_OPERATIONAL_PLUS      = ("card-operational-rune-plus", "+")
        R_OPERATIONAL_MINUS     = ("card-operational-rune-minus", "-")
        R_OPERATIONAL_MULTIPLY  = ("card-operational-rune-multiplication", "*")
        R_OPERATIONAL_DIVIDE    = ("card-operational-rune-division", "/")

    def __init__(self, type: RuneCard.Type, *args, **kwargs):
        self.__type = type
        super().__init__(Configuration.engine_assets_dir / 'images' / 'cards' / f'{type.value[0]}.png', *args, **kwargs)

    def getType(self) -> RuneCard.Type:
        return self.__type
    
    def getValue(self) -> int:
        return self.__type.value[1]
    
    
    

