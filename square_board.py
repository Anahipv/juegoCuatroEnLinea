from linea_board import LinearBoard
from settings import BOARD_LENGTH
from list_utils import displace_matrix, reverse_matrix, transpose, replace_all_in_matrix, collapse_matrix
from string_utils import explode_list_of_strings


class SquareBoard():
    """
    Representa un tablero cuadrado
    """

    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una list de LnearBoard
        """
        board = cls()
        board._columns = list(map(lambda e : LinearBoard.fromList(e), list_of_lists))
        return board
    
    @classmethod
    def fromBoardCode(cls, board_code):
        return cls.fromBoardRawCode(board_code.raw_code)

    @classmethod
    def fromBoardRawCode(cls, board_raw_code):
        """
        Transforma una cadena en formato de BoardCode en una 
        lista de LinearBoards y luego lo transfroma en un tablero cuadrado
        """
        list_of_strings = board_raw_code.split("|")
        matrix = explode_list_of_strings(list_of_strings)
        matrix = replace_all_in_matrix(matrix, '.', None)
        return cls.fromList(matrix)

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def is_full(self):
        """
        True si todos los LinearBoard estan llenos
        """
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result

    def add(self, char, column):
        self._columns[column].add(char)

    def as_matrix(self):
        """
        Devuelve una representacion del tablero como una matriz (lista de listas)
        """
        ### esto fue necesario porque transpose solo trabaja con matrices, LineBoard es un objeto no una lista
        # matrix = []
        # for lb in self._columns:
        #     matrix = matrix.append(lb._column)
        # return matrix

        return list(map(lambda x : x._column, self._columns))
    
    def as_code(self):
        return BoardCode(self)

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        # transposed = transpose(self._columns) ----- self._columns es una lista de objetos, no de listas. No funciona transpose()
        transposed = transpose(self.as_matrix())
        temporal = SquareBoard.fromList(transposed)
        return temporal._any_vertical_victory(char)        

    def _any_sinking_victory(self, char):
        displaced = displace_matrix(self.as_matrix())
        temporal = SquareBoard.fromList(displaced)
        return temporal._any_horizontal_victory(char)

    def _any_rising_victory(self, char):
        reversed = reverse_matrix(self.as_matrix())
        temporal = SquareBoard.fromList(reversed)
        return temporal._any_sinking_victory(char)


  
    # dunders
    
    def __repr__(self):
        return f'{self.__class__} : {self._columns}'

    def __len__(self):
        return len(self._columns)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns

    def __hash__(self):
        return hash(self._columns)
    


class BoardCode:

    def __init__(self, board):
        self._raw_code = collapse_matrix(board.as_matrix())

    @property
    def raw_code(self):
        return self._raw_code

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.raw_code == other.raw_code

    def __hash__(self):
        return hash(self.raw_code)

    def __repr__(self):
        return f'{self.__class__}: {self.raw_code}'
