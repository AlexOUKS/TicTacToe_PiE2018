class Player:

    def __init__(self):
        self.isTurn = False
        self.name = ""

    def getisTurn(self):
        return self.isTurn

    def setisTurn(self, bool):
        self.isTurn = bool

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name