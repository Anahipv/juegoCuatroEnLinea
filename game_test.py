import pytest
from game import Game
from square_board import SquareBoard

def test_creation():
    g = Game()
    assert g != None

def test_is_game_over():

    game = Game()
    win_x = SquareBoard().fromList([['o', 'x', 'x', 'x', 'x'],
                                        [None, None, None, None, None ],
                                        [None, None, None, None, None],
                                        [None, None, None, None, None],
                                        [None, None, None, None, None]])

    win_o = SquareBoard().fromList([['x', 'o', 'x', 'o','o'],
                                        ['x', 'x', 'o', None, None ],
                                        ['o', 'o', None, None, None],
                                        ['o', 'x', None, None, None],
                                        ['x', None, None, None, None]])

    unfinished = SquareBoard().fromList([['x', 'o', None, None, ],
                                        ['o', 'x', None, None, ],
                                        ['x', 'o', None, None, ],
                                        ['x', 'o', None, None, ]])

    tie = SquareBoard().fromList([['x', 'o', 'o', 'x', ],
                                        ['o', 'x', 'x', 'o', ],
                                        ['x', 'o', 'o', 'x', ],
                                        ['o', 'x', 'x', 'o', ]])

    game.board = win_x
    assert game._is_game_over() == True
    game.board = win_o
    assert game._is_game_over() == True
    game.board = unfinished
    assert game._is_game_over() == False
    game.board = tie
    assert game._is_game_over() == True