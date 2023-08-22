from enum import Enum
from copy import deepcopy
from settings import BOARD_LENGTH
from square_board import SquareBoard
from functools import reduce

class ColumnClassification(Enum):
    FULL = -1   #no se puede jugar
    BAD = 1    #podria perder
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
        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL
        
        return ColumnRecommendation(index, classification)
    
    def no_good_options(self, board, player):

        columnRecommendations = self.get_recommendation(board, player)
        #result = reduce(lambda accum, rec : accum + ((rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE)), columnRecommendations, True )
        result = True
        for rec in columnRecommendations:
            if (rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE):
                result = False
                break
        return result
    
class SmartOracle(BaseOracle):

    def _get_column_recommendation(self, board, index, player):
        recommendation =  super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.BAD
        return recommendation
    
    def _is_winning_move(self, board, index, player):
        """
        Determina si un movimiento es una jugada ganadora
        """
        tmp = self._play_on_tmp_board(board, index, player)
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
        will_BAD = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp_board, i, player.opponent):
                will_BAD = True
                break
        return will_BAD
    
class MemoizingOracle(SmartOracle):

    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}

    def _make_key(self, board_code, player):
        """
        La clave combina el board y el player como un string
        """
        return f'{board_code}@{player.char}'

    def get_recommendation(self, board, player):
        key = self._make_key(board.as_code(), player)
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)
        return self._past_recommendations[key]
    
class LearningOracle(MemoizingOracle):
    
    def update_to_bad(self, board_code, player, position):
        key = self._make_key(board_code, player)
        recommendation = self.get_recommendation(SquareBoard.fromBoardCode(board_code), player)
        recommendation[position] = ColumnRecommendation(position, ColumnClassification.BAD)
        self._past_recommendations[key] = recommendation



