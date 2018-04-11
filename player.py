class Player:

    def __init__(self):
        self.isTurn = False

    def getisTurn(self):
        return self.isTurn

    def setisTurn(self, bool):
        self.isTurn = bool