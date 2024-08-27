import unittest
from chess import Chess
from piece import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_turno_inicial(self):
        self.assertNotEqual(self.chess.turn, 'BLACK')
    
    def test_cambio_turno(self):
        self.assertNotEqual(self.chess.turn, 'BLACK')
        self.chess.change_turn()
        self.assertNotEqual(self.chess.turn, 'WHITE')
        self.chess.change_turn()
        self.assertNotEqual(self.chess.turn, 'BLACK')        

if __name__ == '__main__':
    unittest.main()