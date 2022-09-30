from oracle import BaseOracle, ColumnClasification, ColumnRecommendation

class Player():

    def __init__(self, name, char, oracle = BaseOracle()):
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oraculo y juega
        """
        ## Primera aproximacion ##
        #obtener las recomendaciones
        #recommendations = self._oracle.get_recommendation(board, self)
        #selecciona la mejor de todas
        #best = self._choose(recommendations)
        #juega en ella
        #board.add(self.char, best.index)

        ## Refactor ##
        #pregunto al oraculo
        (best, recommendations) = self._ask_oracle(board)
        #juego en la mejor opcion
        self._play_on(board, best.index)

    def _play_on(self, board, position):
        """
        Juega la ficha en la posición indicada
        """
        board.add(self.char, position)

    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devuelve la mejor opción
        """
        recommendations = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendations)
        return (best, recommendations)

    def _choose(self, recommendations):
        #selecciona la mejor opcion de la lista de recomendaciones
        valid = list(filter(lambda x : x.classification != ColumnClasification.FULL, recommendations))
        #agarramos la primera de la lista de validas
        return valid[0]

class HumanPlayer(Player):
    
    def __init__(self, name, char):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """
        El humano es mi oráculo
        """
        while True:
            #pedimos una columna a nuestro humano
            raw = input('Select a column (or h for help): ')
            #verificamos que su respuesta este correcta
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                position = int(raw)
                return (ColumnRecommendation(position, None), None)
            elif raw == "h":
                recommendations = self._oracle.get_recommendation(board, self)
                best = self._choose(recommendations)
                return (best, recommendations)

#Funciones de validación de índice de columna
def _is_within_column_range(board, column):
    return column >= 0 and column < len(board)

def _is_non_full_column(board, column):
    return not board._columns[column].is_full()

def _is_int(num):
    try:
        int(num)
        return True
    except ValueError:       
        return False
