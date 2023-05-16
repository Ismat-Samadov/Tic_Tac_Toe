def draw_board(board):
    """Draws the Tic Tac Toe board."""
    print('-------------')
    for row in board:
        print('|', end=' ')
        for col in row:
            print(col, '|', end=' ')
        print('\n-------------')


def get_move(player):
    """Gets a move from the player and validates it."""
    while True:
        try:
            move = int(input(f"{player}'s turn (1-9): "))
            if 1 <= move <= 9:
                return move
            print("Invalid move. Please enter a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_win(board, player):
    """Checks if the player has won."""
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def play_game():
    """Plays a game of Tic Tac Toe."""
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = 0
    draw_board(board)
    for i in range(9):
        move = get_move(players[current_player])
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] != ' ':
            print("Invalid move. That space is already taken.")
            continue
        board[row][col] = players[current_player]
        draw_board(board)
        if check_win(board, players[current_player]):
            print(f"{players[current_player]} wins!")
            return
        current_player = (current_player + 1) % 2
    print("It's a tie!")


# Play the game
play_game()
