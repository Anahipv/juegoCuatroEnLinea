import pytest
from linea_board import *
from settings import board_length, victory_strike

def test_empty_board():
    empty = LinearBoard()

    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    b = LinearBoard()

    for i in range(board_length):
        b.add('x')
    assert b.is_full() == True
    
def test_victory():
    b = LinearBoard()

    for i in range(victory_strike):
        b.add('x')

    assert b.is_victory('o') == False
    assert b.is_victory('x') == True

def test_tie():
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x', 'o')

def test_add_to_full():
    full = LinearBoard()
    for i in range(board_length):
        full.add('x')

    full.add('x')
    assert full.is_full()