from application.entities.TableEntity import TableEntity

class Player(TableEntity):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)