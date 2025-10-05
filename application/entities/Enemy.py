
from application.entities.TableEntity import TableEntity


class Enemy(TableEntity):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

    def turn(self):
        lowerDeckSpecs = self.getLowerDeckSpecs()
        lowerDeckSpecsIsAllNone = all(el is None for el in lowerDeckSpecs)

        print(lowerDeckSpecsIsAllNone)