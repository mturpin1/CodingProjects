board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 'X'
marks_on_board = 0
def display_board(board):
    print(f'{board[0]}  | {board[1]} |  {board[2]} ')
    print(f'===========')
    print(f'{board[3]}  | {board[4]} |  {board[5]} ')
    print(f'===========')
    print(f'{board[6]}  | {board[7]} |  {board[8]} ')
def mark(player, idx):
    board[idx] = player
def valid_move(idx):
    if board[idx] == ' ':    
        return True
    else:
        return False
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
def check_win(board, player):
    return(
        (board[0] == player and board[1] == player and board[2] == player) or 
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player)
    )
print('''Welcome to Python Tic Tac Toe.
The board is numbered from left to right, top to bottom like this:\n''')
display_board([1,2,3,4,5,6,7,8,9])
print('\nX will start the game. Begin by typing the number of the box you want to fill.')
while marks_on_board < 9:
    move = int(input(f'\nWhich spot will {current_player} choose? ')) - 1
    if valid_move(move):
        mark(current_player, move)
        print()
        display_board(board)
        if check_win(board, current_player):
            print(f'\n{current_player} wins!\n')
            break
        switch_player()
        marks_on_board += 1
    else:
        print('\nThat is not a valid move.\n')
        display_board(board)
if marks_on_board == 9:
    print('\nCat game!\n')
     
