class Piece:
    def __init__(self,color):
        self.color = color
        
        
        def move(self, board, row, column):
            raise NotImplementedError("This method should be overridden by subclasses")
                
class Pawn(Piece):
    pass
class Rook(Piece):
    pass
class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass
    