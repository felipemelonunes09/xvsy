
from application.Actions import Actions
from application.entities.TableEntity import TableEntity
from application.objects.cards.Rune import RuneCard

class Enemy(TableEntity):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

    def turn(self):
        
        lowerDeckSpecs = self.getLowerDeckSpecs()
        lowerDeckSpecsIsAllNone = all(el is None for el in lowerDeckSpecs)

        if (lowerDeckSpecsIsAllNone):
            return Actions.GET_CARD_FROM_RUNE_DECK
        return Actions.GET_CARD_FROM_RUNE_DECK
    
    def addRune(self, rune: RuneCard) -> tuple[int, int]:
        print("add rune trigger")
        if self.getRuneFrame().isFull():
            pass
        else:
            for i, runeFrame in enumerate(self.getRuneFrame().runesFrame):
                if (not runeFrame.hasCard()):
                    runeFrame.setCard(rune)
                    return runeFrame.rect.topleft
