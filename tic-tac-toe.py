import random

# Display the board
def disply_board(board):
    print('\n'*100)
    print(board[7] + " | " + board[8] + " | " + board[9] )
    print('--- --- ---')
    print(board[4] + " | " + board[5] + " | " + board[6] )
    print('--- --- ---')
    print(board[1] + " | " + board[2] + " | " + board[3] ) 

# test_board =['#' , 'X','O','X','O','X','O','X','O','X']*10
# disply_board(test_board)
# disply_board(test_board)

# Ask for marker choice from first player
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Choose X or O : ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else :
        player2 = 'X'
    return(player1,player2)
# player_input()

# place the marker at a position
def place_marker(board, marker ,position):
    board[position] = marker
# place_marker(test_board,'$',8)
# disply_board(test_board)

# Winning conditions
def win_check(board,mark):
    return(
    # Rows
    (board[1] == board[2] == board[3] == mark) or 
    (board[4]== board[5]==board[6] == mark) or 
    (board[7]== board[8] == board[9] == mark) or
    # Columns
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3]== board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or  #Diagonal
    (board[3] == board[5] == board[7] == mark)) #Diagonal
# disply_board(test_board)
# print(win_check(test_board,'X'))

# Choose which player to start randomly
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
# Check for empty position on board 
def space_check(board, position):
    return board[position] == ' '

# Check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Ask for next position of the player
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int (input('Choose a position (1-9): '))
    return position

# replay the game
def replay():
    choice =  input('Play again : Enter Yes/No ')
    return choice == 'Yes'

print('---------------------------WELCOME TO TIC-TAC-TOE-----------------------------------')
while True:
    the_board = [' ']*10
    player1_marker , player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first...')
    play_game = input('Ready to play?? Yes/No')
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
    # GAME PLAY
    while game_on :
        if turn == 'Player 1':
            # show the board
            disply_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position choosen
            place_marker(the_board,player1_marker,position)
            # check if won 
            if win_check(the_board,player1_marker):
                disply_board(the_board)
                print ("PLAYER 1 WON !!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    disply_board(the_board)
                    print('GAME IS A TIE')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # show the board
            disply_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position choosen
            place_marker(the_board,player2_marker,position)
            # check if won 
            if win_check(the_board,player2_marker):
                disply_board(the_board)
                print ("PLAYER 2 WON !!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    disply_board(the_board)
                    print('GAME IS A TIE')
                    game_on = False
                else:
                    turn = 'Player 1'
            
    if not replay():
        break