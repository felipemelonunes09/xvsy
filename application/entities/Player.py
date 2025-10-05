from application.entities.TableEntity import TableEntity

class Player(TableEntity):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

    def turn(self):
        ## improve this logic of hasDroppedAndConsume, maybe use when the users clicks on the deck
        ## also should be two diferent of runeFrames, some RuneFrame shoube of the player and other runeframes will be created to  use for UI
        for frame in self.getRuneFrame().runesFrame:
            if (frame.hasDroppedAndConsume()):
                self.getRuneCardFromDeck()
        if self.getCardHand().hasDroppedAndConsume():
            self.getRuneCardFromDeck()

        return super().turn()
