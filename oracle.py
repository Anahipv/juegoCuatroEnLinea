from enum import Enum, auto

from square_board import SquareBoard

class ColumnClasification(Enum):
    FULL = auto()
    MAYBE = auto()

class ColumnRecommendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    #sobre carga del metodo __eq__() cuando se usa == para comparar python llama a este metodo para comparar
    def __eq__(self, other):
        #si son clases distintas
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, comparo sus propiedades
        else:
            return (self.index, self.classification) == (other.index, other.classification)

    #genera una firma alfanumerica representativa del objeto
    def __hash__(self):
        return hash((self.index, self.classification))

class BaseOracle():

    def get_recommendation(self, board, player):
        """
        Retorna una lista de ColumnRecommendations
        """
        recommendations = []
        for i in range(board.__len__()):
            recommendations.append(self._get_column_recommendation(board, i, player))
        return recommendations

    def _get_column_recommendation(self, board, index, player):
        """
        Clasifica una columna como FULL or MAYBE y retorna una ColumnRecommendation
        """
        classification = ColumnClasification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClasification.FULL
        
        return ColumnRecommendation(index, classification)


board1 =  SquareBoard.fromList([[None, None, None, None],
                                 ['x', 'o', 'x', 'o'],
                                 ['o', 'o', 'x', 'x'],
                                 ['o', None, None, None]])

rappel = BaseOracle()

print(len(rappel.get_recommendation(board1, None)))
print(rappel.get_recommendation(board1, None))