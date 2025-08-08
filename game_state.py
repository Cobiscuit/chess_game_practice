class Game:
    def __init__(self):
        self.board = Board()

    def legal_moves(self):
        # generate pseudo-legal then filter by king safety
        ...
