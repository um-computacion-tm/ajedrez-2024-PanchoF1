import unittest
from pawn import Pawn
from board import Board


class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )
    
    
    def test_not_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )
if __name__ == '__main__':
    unittest.main()        