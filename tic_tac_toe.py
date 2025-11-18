def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    return all(space in ['X', 'O'] for space in board)

def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, enter a position (1-9): ")
        if move.isdigit():
            idx = int(move) - 1
            if 0 <= idx < 9 and board[idx] not in ['X', 'O']:
                return idx
        print("Invalid move! Try again.")

def play_tic_tac_toe():
    while True:
        board = [str(i+1) for i in range(9)]
        current_player = 'X'
        winner = None

        while True:
            print_board(board)
            idx = get_player_move(board, current_player)
            board[idx] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!\n")
                winner = current_player
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!\n")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        again = input("Play again? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for playing Tic-Tac-Toe!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()