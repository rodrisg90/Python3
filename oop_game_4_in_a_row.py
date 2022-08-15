from IPython.display import clear_output

class FourInARow:

    def __init__(self, rows, columns):
        """Inicializa el estado de la clase."""
        self._rows = rows
        self._columns = columns
        self._board = self.building_board()
        self._turn = None

    def building_board(self):
        board = [None] * self._rows
        for r in range(self._rows):
            board[r] = ['.'] * self._columns
        return board

    def print_board(self):
        """Muestra el tablero por pantalla."""
        # Sacamos por pantalla la cabecera
        for num in range(self._columns):
            print(num, end='  ')
        # Sacamos por pantalla el tablero
        for row in self._board:
            print("")
            for box in row:
                print(box, end="  ")

    def insert_token(self, column, color):
        """Esta funcion introduce una ficha en el tablero indicado."""
        if column >= self._columns or column < 0:
            print("ERROR: Numero de columna fuera del rango.")
            return
        elif self._board[0][column] != '.':
            print("ERROR: La columna esta llena de fichas")
            return
        else:
            for row in range(self._rows-1, -1, -1):
                if self._board[row][column] == '.':
                    self._board[row][column] = color
                    return

    def _checking_rows(self, color):
        # Recorremos las filas en busca de 4 en raya
        for r in range(self._rows):
            for c in range(self._columns - 3):
                if self._board[r][c] == color and self._board[r][c+1] == color and self._board[r][c+2] == color and self._board[r][c+3] == color:
                    return True

    def _checking_columns(self, color):
        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns):
            for r in range(self._rows - 3):
                if self._board[r][c] == color and self._board[r+1][c] == color and self._board[r+2][c] == color and self._board[r+3][c] == color:
                    return True

    def _checking_right_diagonal(self, color):
        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns - 3):
            for r in range(self._rows-1, 2, -1):
                if self._board[r][c] == color and self._board[r-1][c+1] == color and self._board[r-2][c+2] == color and self._board[r-3][c+3] == color:
                    return True

    def _checking_left_diagonal(self, color):
        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns-1, 2, -1):
            for r in range(self._rows-1, 2, -1):
                if self._board[r][c] == color and self._board[r-1][c-1] == color and self._board[r-2][c-2] == color and self._board[r-3][c-3] == color:
                    return True

    def checking_winner(self, color):
        """Comprueba si ha salido un cuatro en raya."""
        return self._checking_rows(color) or self._checking_columns(color) or self._checking_right_diagonal(color) or self._checking_left_diagonal(color)

    def play(self, player1 = 'X', player2 = 'O'):
        self._turn = player2
        while True:
            self._turn = player1 if self._turn == player2 else player2
            self.print_board()
            column = int(input("Turno del jugador {}: ".format(self._turn)))
            self.insert_token(column, self._turn)
            clear_output(wait=False)
            if self.checking_winner(self._turn):
                print("\n\nEl ganador es el jugador {}!\n\n".format(self._turn))
                self.print_board()
                break

game = FourInARow(6, 7)
game.play()

