import pyfiglet
from match import Match
from enum import Enum, auto
from player import Player, HumanPlayer, ReportingPlayer
from square_board import SquareBoard
from list_utils import reverse_matrix
from settings import BOARD_LENGTH
from beautifultable import BeautifulTable
from oracle import BaseOracle, SmartOracle, LearningOracle

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class Game():

    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(ReportingPlayer('chip'), ReportingPlayer('chop'))):
        self.round_type = round_type
        self.match = match
        self.board = SquareBoard()

    def start(self):
        #imprimo el nombre del juego
        self.print_logo()
        #configuro la partida
        self._configure_by_user()
        #arranco el game loop
        self._start_game_loop()
    
    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print(logo.renderText('Connecta'))

    def _start_game_loop(self):
        #bucle infinito
        while True:
            #obtengo el jugador de turno
            current_player = self.match.next_player
            #le hago jugar
            current_player.play(self.board)
            #muestro su jugada
            self.display_move(current_player)
            #imprimo el tablero
            self.display_board()
            #si el juego ha terminado...
            if self._is_game_over():
                #muestro el resultado final
                self.display_result()
                #salgo del bucle
                break
    
    def display_move(self, player):
        print(f'\n{player.name} ({player.char}) has moved in column {player.last_moves[0].position}')

    def display_board(self):
        """
        Imprime el tablero en su estado actual
        """
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        print(bt)

    def display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f'\n{winner.name} ({winner.char}) wins!!!')
        else:
            print(f'\nA tie beetween {self.match.get_player("x").name} (x) and {self.match.get_player("o").name} (o)')

    def _is_game_over(self):
        """
        El juego se acaba cuando hay un vencedor o empate
        """
        ## return self.board.is_full() or self.board.is_victory('x') or self.board.is_victory('o')

        winner = self.match.get_winner(self.board)
        if winner != None:
            #hay un vencedor
            return True
        elif self.board.is_full():
            #empate
            return True
        else:
            return False

    def _configure_by_user(self):
        """
        El usuario puede elegir que tipo de partida quiere y nivel de dificultad
        """
        #determinar el tipo de partida
        self.round_type = self._get_round_type()
        #preguntar nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()
        #crear la partida
        self.match = self._make_match()

    def _get_round_type(self):
        print("-.-.-.-.-.-.-.-.-\nSelect type of round:\n1- Computer vs Computer\n2- Computer vs Human\n-.-.-.-.-.-.-.-.-")
        response = ""
        while response != "1" and response != "2":
            response = input('Please type either 1 or 2: ')
        if response == "1":
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def _get_difficulty_level(self):
        """
        Pregunta el nivel de dificultad del jugador computadora
        """
        print("""
        Chose your opponent, human:

        1) Bender: for clowns and wimps
        2) T-800: you may regret it
        3) T-1000: Don't even think about it!
        """)

        while True:
            response = input('Please type 1, 2 or 3: ').strip()
            if response == '1':
                level = DifficultyLevel.LOW
                break
            elif response == '2':
                level = DifficultyLevel.MEDIUM
                break
            else:
                level = DifficultyLevel.HIGH
                break
        return level

    def _make_match(self):
        """
        Player 1 siempre sera robotico
        """

        _levels = {DifficultyLevel.LOW : BaseOracle(), 
                   DifficultyLevel.MEDIUM : SmartOracle(), 
                   DifficultyLevel.HIGH : LearningOracle()}

        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #ambos jugadores son roboticos
            player1 = ReportingPlayer('R2', oracle=LearningOracle())
            player2 = ReportingPlayer('3PO', oracle= LearningOracle())
        else:
            #hay un jugador humano
            player1 = ReportingPlayer('R2', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=input("Ingresa tu nombre: "))
            player2._oracle = _levels[self._difficulty_level]
        
        return Match(player1, player2)