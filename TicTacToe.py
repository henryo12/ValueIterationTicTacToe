
import sys
import numpy as np
import time

def CheckWinner(board):
    colSum = board.sum(0)
    rowSum = board.sum(1)
    diag1Sum = board[0][0] + board[1][1] + board[2][2]
    diag2Sum = board[0][2] + board[1][1] + board[2][0]
    if(max(colSum.max(),rowSum.max(),diag1Sum,diag2Sum)==3):
        print('Player 1 wins!')
        return 1
    elif(min(colSum.min(),rowSum.min(),diag1Sum,diag2Sum)==-3):
        print('Player 2 wins!')
        return 2
    elif(np.where(board==0)[0].size==0):
        print('Tie!')
        return 0
    else:
        return None
        
def dispBoard(board):
    print(num2xo(board[0][0])+'|'+num2xo(board[0][1])+'|'+num2xo(board[0][2]))
    print('-----')
    print(num2xo(board[1][0])+'|'+num2xo(board[1][1])+'|'+num2xo(board[1][2]))
    print('-----')
    print(num2xo(board[2][0])+'|'+num2xo(board[2][1])+'|'+num2xo(board[2][2]))
    
    
def num2xo(num):
    if num == 1:
        return 'x'
    elif num == -1:
        return 'o'
    else:
        return ' '
        
def CompPlayer(b,states,moves,compNum):
    exists = 0
    for i in range(len(states)):
        if np.array_equal(states[i],b):
            m = moves[i]
            print(m)
            exists = 1
            break
    if not exists:
        print('error, board not found')
        sys.exit()
        
    b[m[0]][m[1]] = compNum
    return b
    

if __name__ == '__main__':
    statesP1 = list(np.load('statesP1.npy'))
    statesP2 = list(np.load('statesP2.npy'))
    idealMoveP1 = list(np.load('idealMoveP1.npy'))
    idealMoveP2 = list(np.load('idealMoveP2.npy'))
    
    board = np.zeros((3,3)).astype(int)
    
    print('Player 1 is x\'s, and player 2 is o\'s')
    human = input('Enter 1 or 2 to play as player 1 or 2: ')
    
    if human == '1':
        statesComp = list(np.load('statesP2.npy'))
        idealMoveComp = list(np.load('idealMoveP2.npy'))
        humanNum = 1
        compNum =  -1
    elif human == '2':
        statesComp = list(np.load('statesP1.npy'))
        idealMoveComp = list(np.load('idealMoveP1.npy'))
        humanNum = -1
        compNum = 1
    else:
        print('Please try again and enter 1 or 2.')
        sys.exit()
    
    turn = int(human) - 1
    winner = CheckWinner(board)
        
    while(winner == None):
        if(turn == 0):
            waitForMove = True
            while(waitForMove):
            #print('player1')
                move = input('Enter the row and column you would like to place your move (ex: 0,1): ')
                try:
                    move = move.split(',',2)
                    row = int(move[0])
                    col = int(move[1])
                    if board[row][col] != 0:
                        print('Invalid move. Try again.')
                        continue
                except:
                    print('Invalid move. Try again.')
                    continue
                waitForMove = False
                board[row][col] = humanNum
                print('Board after your turn: ')
                dispBoard(board)
        else:
            #print('player2')
            
            board = CompPlayer(board,statesComp,idealMoveComp,compNum)
            print('Board after computer\'s turn: ')
            dispBoard(board)
        time.sleep(1)
        winner = CheckWinner(board)
        turn = 1 - turn
            

    
    