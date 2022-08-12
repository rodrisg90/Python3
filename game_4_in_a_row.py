from IPython.display import clear_output

def bulding_board(rows, columns):
    """Crea el tablero de juego.

    Parametros posicionales
    filas -- int que represente el numero de filas del tablero.
    columnas -- int que represente el numero de columnas del tablero.
    """
    board = [None] * rows
    for r in range(rows):
        board[r] = ['.'] * columns
    return board

def print_board(board):
    """Muestra el tablero por pantalla."""
    # Sacamos por pantalla la cabecera
    for num in range(len(board[0])):
        print(num, end='  ')
    # Sacamos por pantalla el tablero
    for row in board:
        print("")
        for box in row:
            print(box, end="  ")

def insert_token(board, column, color):
    """Esta funcion introduce una ficha en el tablero indicado."""
    if column >= len(board[0]) or column < 0:
        print("ERROR: Numero de columna fuera del rango.")
        return
    elif board[0][column] != '.':
        print("ERROR: La columna esta llena de fichas")
        return
    else:
        for row in range(len(board)-1, -1, -1):
            if board[row][column] == '.':
                board[row][column] = color
                return board

def checking_rows(board, color):
    # Obtenemos el numero de filas y columnas
    num_rows = len(board)
    num_columns = len(board[0])
    # Recorremos las filas en busca de 4 en raya
    for r in range(num_rows):
        for c in range(num_columns - 3):
            if board[r][c] == color and board[r][c+1] == color and board[r][c+2] == color and board[r][c+3] == color:
                return True

def checking_columns(board, color):
    # Obtenemos el numero de filas y columnas
    num_rows = len(board)
    num_columns = len(board[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columns):
        for r in range(num_rows - 3):
            if board[r][c] == color and board[r+1][c] == color and board[r+2][c] == color and board[r+3][c] == color:
                return True

def checking_right_diagonal(board, color):
    # Obtenemos el numero de filas y columnas
    num_rows = len(board)
    num_columns = len(board[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columns - 3):
        for r in range(num_rows-1, 2, -1):
            if board[r][c] == color and board[r-1][c+1] == color and board[r-2][c+2] == color and board[r-3][c+3] == color:
                return True

def checking_left_diagonal(board, color):
    # Obtenemos el numero de filas y columnas
    num_rows = len(board)
    num_columns = len(board[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columns-1, 2, -1):
        for r in range(num_rows-1, 2, -1):
            if board[r][c] == color and board[r-1][c-1] == color and board[r-2][c-2] == color and board[r-3][c-3] == color:
                return True

def checking_winner(board, color):
    """Comprueba si ha salido un cuatro en raya."""
    return checking_rows(board, color) or checking_columns(board, color) or checking_right_diagonal(board, color) or checking_left_diagonal(board, color)

board = bulding_board(6, 7)
turn = 'O'
next_turn = 'X'
while True:
    turn = next_turn
    print_board(board)
    if turn == 'O':
        column = int(input("Turno del círculo: "))
        next_turn = 'X'
    elif turn == 'X':
        column = int(input("Turno de la cruz: "))
        next_turn = 'O'
    insert_token(board, column, turn)
    clear_output(wait=False)
    if checking_winner(board, turn):
        print("El ganador es el jugador ", turn, "\n\n")
        print_board(board)
        break

