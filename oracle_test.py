from oracle import *
from player import Player
from settings import BOARD_LENGTH
from square_board import SquareBoard


def test_base_oracle():
    board =  SquareBoard.fromList([[None, None, None, None],
                                 ['x', 'o', 'x', 'o'],
                                 ['o', 'o', 'x', 'x'],
                                 ['o', None, None, None]])

    expected = [ColumnRecommendation(0, ColumnClasification.MAYBE),
                ColumnRecommendation(1, ColumnClasification.FULL),
                ColumnRecommendation(2, ColumnClasification.FULL),
                ColumnRecommendation(3, ColumnClasification.MAYBE),]

    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    # assert rappel.get_recommendation(board, None) == expected
    assert rappel.get_recommendation(board, None) == expected

def test_equality():
    cr = ColumnRecommendation(2, ColumnClasification.MAYBE)

    assert cr == cr
    assert cr == ColumnRecommendation(2, ColumnClasification.MAYBE)
    assert cr != ColumnRecommendation(2, ColumnClasification.WIN)
    assert cr != ColumnRecommendation(3, ColumnClasification.FULL)

def test_is_winning_move():
    winner = Player('Player1', 'x')
    loser = Player('Player2', 'o')

    empty = SquareBoard()
    almost = SquareBoard.fromList([['o', 'x', 'o', None],
                                   ['o', 'x', 'o', None],
                                   ['x', None, None, None],
                                   [None, None, None, None]])
    
    oracle = SmartOracle()

    # sobre el tablero vacio
    for i in range(0, BOARD_LENGTH):
            assert oracle._is_winning_move(empty, i, winner) == False
            assert oracle._is_winning_move(empty, i, loser) == False

    # sobre el tablero de verdad
    for i in range(0, BOARD_LENGTH):
         assert oracle._is_winning_move(almost, i, loser) == False

    assert oracle._is_winning_move(almost, 2, winner)

def test_is_losing_move():
    winner = Player('Player1', 'x')
    loser = Player('Player2', 'o')

    winner.opponent = loser

    empty = SquareBoard()
    almost = SquareBoard.fromList([['o', 'x', 'o', None],
                                   ['o', 'x', 'o', None],
                                   ['x', None, None, None],
                                   [None, None, None, None]])
    
    oracle = SmartOracle()
    
    for i in range(0, BOARD_LENGTH):
        assert oracle._is_losing_move(empty, i, winner) == False
        assert oracle._is_losing_move(empty, i, loser) == False

    assert oracle._is_losing_move(almost, 0, loser)
    assert oracle._is_losing_move(almost, 3, loser) 