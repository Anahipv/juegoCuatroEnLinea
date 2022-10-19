import pytest
from player import Player, HumanPlayer
from match import Match

#esta funcion se ejecuta antes de cada test para crear el entorno del test
def setup():
    global dona
    dona = HumanPlayer('Dona')
    global cookie
    cookie = Player('Cookie')

#esta funcion se ejecuta luego de cada test y limpia el entorno
def teardown():
    global dona
    dona = None
    global cookie
    cookie = None

def test_different_players_have_different_chars():
    t = Match(dona, cookie)
    assert dona.char != cookie.char

def test_no_player_with_none_char():
    t = Match(dona, cookie)
    assert dona.char != None
    assert cookie.char != None

def test_next_player_is_round_robbin():
    t = Match(dona, cookie)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

def test_player_are_opponents():
    t = Match(dona, cookie)
    p1 = t.get_player('x')
    p2 = t.get_player('o')
    assert p1.opponent == p2
    assert p2.opponent == p1
