import unittest
from board import Board  
from rook import Rook 
from bishop import Bishop 
from knight import Knight 
from queen import Queen 
from king import King

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_pos_iniciales(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), King)
        self.assertIsInstance(self.board.get_piece(0, 4), Queen)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)


    def test_obtener_pieza(self):
        piece = self.board.get_piece(0, 4)
        self.assertIsInstance(piece, Queen)



if __name__ == '__main__':
    unittest.main()