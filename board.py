from rook import Rook
from king import King
from knight import Knight
from queen import Queen
from bishop import Bishop
from pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("WHITE") # white posiciones
        self.__positions__[0][1] = Knight("WHITE") 
        self.__positions__[0][2] = Bishop("WHITE") 
        self.__positions__[0][3] = King("WHITE") 
        self.__positions__[0][4] = Queen("WHITE")         
        self.__positions__[0][5] = Bishop("WHITE") 
        self.__positions__[0][6] = Knight("WHITE") 
        self.__positions__[0][7] = Rook("WHITE") 

        for col in range(8):
            self.__positions__[1][col] = Pawn("WHITE")
            self.__positions__[6][col] = Pawn("BLACK")

        self.__positions__[7][0] = Rook("BLACK") # black posiciones
        self.__positions__[7][1] = Knight("BLACK") 
        self.__positions__[7][2] = Bishop("BLACK") 
        self.__positions__[7][3] = King("BLACK") 
        self.__positions__[7][4] = Queen("BLACK")         
        self.__positions__[7][5] = Bishop("BLACK") 
        self.__positions__[7][6] = Knight("BLACK") 
        self.__positions__[7][7] = Rook("BLACK")

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str        

    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
