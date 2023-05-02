from enum import Enum
from copy import deepcopy
from settings import BOARD_LENGTH

from square_board import SquareBoard

class ColumnClasification(Enum):
    FULL = -1   #no se puede jugar
    LOSE = 1    #podria perder
    MAYBE = 10   #indeseable
    WIN = 100   #la mejor opcion: gano

    def __str__(self):
        return f'{vars(self).get("_name_", "UNKNOWN")}'

class ColumnRecommendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    #sobre carga del metodo __eq__() cuando se usa == para comparar python llama a este metodo para comparar
    def __eq__(self, other):
        #si son clases distintas
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, comparo sus propiedades classification
        else:
            return self.classification == other.classification

    #genera una firma alfanumerica representativa del objeto
    def __hash__(self):
        return hash((self.index, self.classification))
    
    def __str__(self):
        return f'{self.index} , {self.classification}'
    
    def __repr__(self):
        return f'{self.index} , {self.classification}'

class BaseOracle():

    def get_recommendation(self, board, player):
        """
        Retorna una lista de ColumnRecommendations
        """
        recommendations = []
        for i in range(board.__len__()):
            recommendations.append(self._get_column_recommendation(board, i, player))
        return recommendations

    def _get_column_recommendation(self, board, index, _):
        """
        Clasifica una columna como FULL or MAYBE y retorna una ColumnRecommendation
        """
        classification = ColumnClasification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClasification.FULL
        
        return ColumnRecommendation(index, classification)
    
class SmartOracle(BaseOracle):

    def _get_column_recommendation(self, board, index, player):
        recommendation =  super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClasification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClasification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClasification.LOSE
        return recommendation
    
    def _is_winning_move(self, board, index, player):
        """
        Determina si un movimiento es una jugada ganadora
        """
        # hago una copia del tablero
        #juego en ella
        tmp = self._play_on_tmp_board(board, index, player)
        #determino si hay una victoria para player o no
        return tmp.is_victory(player.char)
    
    def _play_on_tmp_board(self, board, index, player):
        """
        Crea un copia y juega en el
        """
        tmp_board = deepcopy(board)
        tmp_board.add(player.char, index)
        return tmp_board

    def _is_losing_move(self, board, index, player):
        """
        Si player juega en index, genera una jugada vencedora para el oponente? 
        """
        tmp_board = self._play_on_tmp_board(board, index, player)
        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp_board, i, player.opponent):
                will_lose = True
                break
        return will_lose

