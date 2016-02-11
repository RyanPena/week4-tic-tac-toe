def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def checkWinner(board, player) :
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and bo['top-M'] and bo['top-R'] == player or #Top row
    (board['mid-L'] == player and bo['mid-M'] and bo['mid-R'] == player or #mid
    (board['low-L'] == player and bo['low-M'] and bo['low-R'] == player or #bot
    (board['top-L'] == player and bo['mid-M'] and bo['low-R'] == player or #left
    (board['top-M'] == player and bo['mid-M'] and bo['low-R'] == player or #down mid
    (board['top-R'] == player and bo['mid-M'] and bo['low-R'] == player or #right
    (board['top-L'] == player and bo['mid-M'] and bo['low-R'] == player or #diagonal
    (board['top-R'] == player and bo['mid-M'] and bo['low-R'] == player or #diagonal
    
    
def startGame(startingPlayer, board):
    turn = startingPlayer
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        board[move] = turn 
        if( checkWinner(board, 'X') ): #Checks if X won
            print('X wins!') #X won, this line states that
            break #breaks the loop
        elif ( checkWinner(board, 'O') ): #If X did'nt win, checks if O wins
            print('O wins!') #O won, this line states that
            break #breaks the loop
    
        if turn == 'X': #X's turn
            turn = 'O' #O's turn
        else:
            turn = 'X'
        
    printBoard(board)
    
