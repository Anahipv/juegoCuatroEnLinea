from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import *

## comentarios con doble numeral mi solucion
# comentarios de un solo numeral, comentarios relacionados al video

class LinearBoard():

    """
    Clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacio vacio
    """

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._column = list
        return board

    def __init__(self):
        ##self.line = []

        #Una lista de None
        self._column = [None for i in range(BOARD_LENGTH)]
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._column == other._column

    def __hash__(self):
        return hash(self._column)
    
    def add(self, x):
        """
        Juega en la primera posicion disponible
        """
        ##self.line.append(x)

        #siempre y cuando no este lleno...
        if not self.is_full():
            #buscamos la primera posicion libre (None)
            i = self._column.index(None)
            #lo sustituimos por el paramentro ingresado
            self._column[i] = x

    def is_full(self):
        ##if len(self.line) < BOARD_LENGTH:  
        ##    return False
        ##else:
        ##    return True

        return self._column[-1] != None

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        """
        no hay vitoria ni de char1 ni de char2
        """
        return self.is_victory(char1) == False and self.is_victory(char2) == False
    