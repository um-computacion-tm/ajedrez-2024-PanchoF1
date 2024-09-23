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

    def test_eat_left_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 6)]
        ) 

    def test_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )
                       
if __name__ == '__main__':
    unittest.main()