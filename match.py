class Match():

    def __init__(self, player1, player2):
        #asigna una tipo de ficha a cada jugador
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2
        #guarda a los jugador en un dic para acceder por su char
        self._players = {'x' : player1, 'o' : player2}
        #tambien los guarda en una lista para acceder uno a uno segun el turno
        self._round_robbin = [player1, player2]

    @property
    def next_player(self):
        # guarda en una variable que retorna el jugador que sigue
        next = self._round_robbin[0]
        # invierte la lista
        self._round_robbin.reverse()
        return next

    def get_player(self, char):
        return self._players[char]

    def get_winner(self, board):
        """
        Devuelve el jugador ganador, si no lo hay devuleve None
        """
        if board.is_victory('x'):
            return self.get_player('x')
        elif board.is_victory('o'):
            return self.get_player('o')
        else:
            return None