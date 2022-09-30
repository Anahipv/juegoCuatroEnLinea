from oracle import *
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
    assert cr != ColumnRecommendation(1, ColumnClasification.MAYBE)
    assert cr != ColumnRecommendation(2, ColumnClasification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClasification.FULL)