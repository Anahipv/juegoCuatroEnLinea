from oracle import BaseOracle, ColumnClasification

class Player():

    def __init__(self, name, char, oracle = BaseOracle()):
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oraculo
        """
        #obtener las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        #selecciona la mejor de todas
        best = self._choose(recommendations)
        #juega en ella
        board.add(self.char, best.index)

    def _choose(self, recommendations):
        #selecciona la mejor opcion de la lista de recomendaciones
        valid = list(filter(lambda x : x.classification != ColumnClasification.FULL, recommendations))
        #agarramos la primera de la lista de validas
        return valid[0]


def _is_within_column_range(board, column):
    pass

def _is_non_full_column(board, column):
    pass

def _is_int(num):
    pass