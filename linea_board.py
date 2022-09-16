from settings import board_length, victory_strike
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

    def __init__(self):
        ##self.line = []

        #Una lista de None
        self._column = [None for i in range(board_length)]
    
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
        ##if len(self.line) < board_length:  
        ##    return False
        ##else:
        ##    return True

        return self._column[-1] != None

    def is_victory(self, char):
        return find_streak(self._column, char, victory_strike)

    def is_tie(self, char1, char2):
        """
        no hay vitoria ni de char1 ni de char2
        """
        return self.is_victory(char1) == False and self.is_victory(char2) == False
    