from application.Actions import Actions
from application.entities.TableEntity import TableEntity

class Player(TableEntity):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

    def turn(self):
        ## improve this logic of hasDroppedAndConsume, maybe use when the users clicks on the deck
        ## also should be two diferent of runeFrames, some RuneFrame should of the player and other runeframes will be created to  use for UI
        for frame in self.getRuneFrame().runesFrame:
            if (frame.hasDroppedAndConsume()):
                return Actions.GET_CARD_FROM_RUNE_DECK
            
        if self.getCardHand().hasDroppedAndConsume():
            return Actions.GET_CARD_FROM_RUNE_DECK

        return super().turn()
