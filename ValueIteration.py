# First working version
# Player 1 and Player 2 training against each other

import numpy as np
import random


            
def Player1(board):
    moves = np.where(board==0)
    numMoves = moves[0].size
    move = random.randint(0,numMoves-1)
    board[moves[0][move]][moves[1][move]] = 1
    return board
            
def Player2(board):
    moves = np.where(board==0)
    numMoves = moves[0].size
    move = random.randint(0,numMoves-1)
    board[moves[0][move]][moves[1][move]] = -1
    return board
            
def CheckWinner(board):
    colSum = board.sum(0)
    rowSum = board.sum(1)
    diag1Sum = board[0][0] + board[1][1] + board[2][2]
    diag2Sum = board[0][2] + board[1][1] + board[2][0]
    if(max(colSum.max(),rowSum.max(),diag1Sum,diag2Sum)==3):
        #print('Player 1 wins!')
        return 1
    elif(min(colSum.min(),rowSum.min(),diag1Sum,diag2Sum)==-3):
        #print('Player 2 wins!')
        return 2
    elif(np.where(board==0)[0].size==0):
        #print('Tie!')
        return 0
    else:
        return None
        
def ValueIteration(board,player):
    ...
    #Compute utility of each potential move during each new state
    #Utility of a state depends on the utility of all successor states
    #Utility = reward in current state plus max utility of successor states
    
    #U=ValueIteration(M,R)
        #where M is transition model
        #R is a reward function on states
    #U=U_p=R
    #while(abs(U-U_p)<tol):
    #   U = U_p
    #   for(each state i):
    #   U_p[i] = R[i] + max(M_ij*U[j])
    #       where M_ij is probability of reaching state j from state i with action a
    #       where U[j] is utility of state j
    #
    
    
    #Matlab Code:
    """
    pTrans = 
    controls = [up down left right stay]
    for iter in numIterations
        for row in rows
            for col in cols
                if board(row,col) is empty
                    expectedValue=zeros(contrls,1)
                    for cntrl in cntrls (each possible action)
                        for cntrl_prob in cntrls (transition prob in each direction for a specific attempted direction)
                            idxx = new row after moving according to controls[cntrls_i]
                            idxy = new col after moving according to controls[cntrls_i]
                            if(idxx and idxy are in border and board is empty)
                                expectedValue(cntrl)=expectedValue(cntrl)+U(idxx,idxy)*pTrans(cntrl,cntrl_i)
                            else (hits obstacle, bounces back to stay in same location)
                                expectedValue(cntrl)=expectedValue(cntrl)+U(row,col)*pTrans(cntrl,cntrl_i)
                
                [Ustar,cntrl corresponding to max] = max(expectedValue)
                Control_mat(row,col) = direction you should move from this cell
                Up1(row,col)=gamma*((Reward of cell) + Ustar)
        U=Up1
        U(winRow,winCol)=1
        U(penRow,penCol)=-1
    
                
                
    TicTacToe version:
    When player x is about to make a move:
    
    R = penalty for occupying a state (-1 to 0), doesn't change
        should be all zeros? or potentially reward middle placements, then corner placements
    U = Utility for a state (-1 to 1), changes each iteration
        win=1, loss=-1, draw=-0.1
    
    for iter in numIterations
        for state in states
            possibleMoves = locations of 0's on board
            numPossibleMoves = possibleMoves.size
            expectedValue = zeros(numPossibleMoves,1)
            for move in possibleMoves
                movex = move.x
                movey = move.y
                expectedValue(move) = expectedVale(move)+U(state)*1 #=U(state)
        [Ustar,idealMoveInThisState] = max(expectedValue)
        idealMove(state) = idealMoveInThisState
        Up1(state) = gamma* (R+Ustar) = Ustar   #gamma prob equals 1, R prob equals 0)
    U = Up1
        
        
    instead of iterating through all rows and cols, I need to iterate through all possible states

    """

def StoreState(s,board):
    exists = 0
    for i in range(len(s)):
        if np.array_equal(s[i],board):
            #State already exists
            #print('\n\n')
            #print(s)
            #print(board)
            #print('exists')
            exists = 1
            break
    if not exists:
        #print('appending')
        #print(board)
        s.append(board.copy())
    return s
    
def FindState(s,board):
    for i in range(len(s)):
        if np.array_equal(s[i],board):
            #State already exists
            #print('\n\n')
            #print(s)
            #print(board)
            #print('exists')
            return i
    
def StoreUtil(utilsP1,board):
    winner = CheckWinner(board)
    
def CalcUtils(states):
    u = [0.0]*len(states)
    for i in range(len(states)):
        #print(states[i])
        winner = CheckWinner(states[i])
        if(winner==1):
            u[i] = 1
        elif(winner==2):
            u[i] = -1
        elif(winner==0):
            u[i] = 0 #-0.1
        else:
            u[i] = 0
    return u
    
def CalcUtil(state):
    winner = CheckWinner(state)
    if(winner==1):
        u = 1
    elif(winner==2):
        u = -1
    elif(winner==0):
        u = 0 #-0.1
    else:
        u = 0
    return u
    
def MakeStates():
    board = np.zeros((3,3)).astype(int)
    s9MovesLeft = [board]
    s8MovesLeft = []
    s7MovesLeft = []
    s6MovesLeft = []
    s5MovesLeft = []
    s4MovesLeft = []
    s3MovesLeft = []
    s2MovesLeft = []
    s1MovesLeft = []
    s0MovesLeft = []
    
    for a in range(9):
        row = a//3
        col = a%3
        b1 = board.copy()
        b1[row][col] = 1
        s8MovesLeft.append(b1)
        for b in range(9):
            row = b//3
            col = b%3
            if b1[row][col] == 0:
                b2 = b1.copy()
                b2[row][col] = -1
                s7MovesLeft.append(b2)
                
    return states
            
if __name__ == '__main__':
    try:
        if False:
            s = MakeStates()
        else:
            try:
                statesP1 = list(np.load('statesP1.npy'))
                #utilsP1 = list(np.load('utilsP1.npy'))
                print('Reusing Player 1 states file')
            except:
                statesP1 = [np.zeros((3,3)).astype(int)]
                #utilsP1 = [0]
                print('Starting with no saved states for Player 1')
                
            try:
                statesP2 = list(np.load('statesP2.npy'))
                print('Reusing Player 2 states file')
            except:
                statesP2 = [np.zeros((3,3)).astype(int)]
                print('Starting with no saved states for Player 2')
                
            
            # To make more efficient, have different states arrays for each number of turns
            for i in range(1000):
                board = np.zeros((3,3)).astype(int)
                turn = 1
                winner = None
                while(winner == None):
                    if(turn == 1):
                        #print('player1')
                        
                        #utilsP1 = StoreUtil(utilsP1,board)
                        board = Player1(board)
                        statesP2 = StoreState(statesP2,board)
                        print('P2 states'+str(len(statesP2)))
                    else:
                        #print('player2')
                        
                        board = Player2(board)
                        statesP1 = StoreState(statesP1,board)
                        print('P1 states'+str(len(statesP1)))
                    turn = 1 - turn
                    winner = CheckWinner(board)
                    #print(board)
                    #print(winner)
                    
                    
                print('new game')
            
        #print(statesP1)
        utilsP1 = CalcUtils(statesP1)
        utilsP2 = CalcUtils(statesP2)
        """
        print('Utils1 #:')
        print(len(utilsP1))
        print('Utils2 #:')
        print(len(utilsP2))
        print(utilsP2)
        
        statesP1 = np.asarray(statesP1)
        np.save('statesP1',statesP1)
        statesP2 = np.asarray(statesP2)
        np.save('statesP2',statesP2)
        #print(states)
        statesP1 = list(statesP1)
        statesP2 = list(statesP2)
        """
        
        
        """
        R = penalty for occupying a state (-1 to 0), doesn't change
            should be all zeros? or potentially reward middle placements, then corner placements
        U = Utility for a state (-1 to 1), changes each iteration
            win=1, loss=-1, draw=-0.1
        
        for iter in numIterations
            for state in states
                possibleMoves = locations of 0's on board
                numPossibleMoves = possibleMoves.size
                expectedValue = zeros(numPossibleMoves,1)
                for move in possibleMoves
                    movex = move.x
                    movey = move.y
                    expectedValue(move) = expectedVale(move)+U(state)*1 #=U(state)
            [Ustar,idealMoveInThisState] = max(expectedValue)
            idealMove(state) = idealMoveInThisState
            Up1(state) = gamma* (R+Ustar) = Ustar   #gamma prob equals 1, R prob equals 0)
        U = Up1
        #utilities of finished games are fixed
        U(wins)=1
        U(losses)=-1
        U(ties)=-0.1
        
        """
        idealMoveP1=[0]*len(statesP1)
        idealMoveP2=[0]*len(statesP2)
        #Up1=[0]*len(statesP1)
        #Up2=[0]*len(statesP2)
        gamma=0.9
        
        numIters = 10
        for iter in range(numIters):
            print('Iteration: '+str(iter))
            print('Utils1 #:')
            print(len(utilsP1))
            print('Utils2 #:')
            print(len(utilsP2))
            print(utilsP2)
            for stateP1Num, stateP1 in enumerate(statesP1):
                #print(stateP1)
                winner = CheckWinner(stateP1)
                #print(winner)
                if winner is None:
                    moves = np.where(stateP1==0)
                    rowMoves = list(moves[0])
                    colMoves = list(moves[1])
                    numMoves = len(rowMoves) #moves[0].size
                    #print('State!!!!!!!!!!!!: ')
                    #print(stateP1)
                    #print(numMoves)
                    eVals = [0.0]*numMoves
                    #print(eVals)
                    for i in range(numMoves):
                        #print('Next board: ')
                        nextBoard = stateP1.copy() #.copy()????
                        nextBoard[rowMoves[i]][colMoves[i]] = 1
                        #print(nextBoard)
                        #print('state')
                        #print(stateP1)
                        #statesP2 = StoreState(statesP2,nextBoard)
                        #update utilsP2
                        try:
                            eVals[i] = -1*utilsP2[FindState(statesP2,nextBoard)] # find utility of that board from statesP2
                            #print('P2 state found')
                        except:
                            #print('Adding P2 state')
                            statesP2.append(nextBoard)
                            utilsP2.append(-1*CalcUtil(nextBoard))
                            eVals[i] = utilsP2[-1]
                            
                            #print(utilsP2)
                            
                            idealMoveP2.append(0)
                            #Up2.append(0)
                        #print(eVals[i])
                    #print(eVals)
                    UstarP1 = max(eVals)
                    idealMoveNum = eVals.index(max(eVals))
                    idealMoveP1[stateP1Num] = [rowMoves[idealMoveNum],colMoves[idealMoveNum]]
                    utilsP1[stateP1Num] = gamma * UstarP1
                else:
                    idealMoveP1[stateP1Num] = None
                    if winner == 2:
                        utilsP1[stateP1Num] = -1
                    else: #tie
                        utilsP1[stateP1Num] = 0 #-0.1

            for stateP2Num, stateP2 in enumerate(statesP2):
                winner = CheckWinner(stateP2)
                if winner is None:
                    moves = np.where(stateP2==0)
                    rowMoves = list(moves[0])
                    colMoves = list(moves[1])
                    numMoves = len(rowMoves) #moves[0].size
                    eVals = [0.0]*numMoves
                    for i in range(numMoves):
                        nextBoard = stateP2.copy() #.copy()????
                        nextBoard[rowMoves[i]][colMoves[i]] = -1
                        #statesP2 = StoreState(statesP2,nextBoard)
                        #update utilsP2
                        try:
                            eVals[i] = -1*utilsP1[FindState(statesP1,nextBoard)] # find utility of that board from statesP2
                        except:
                            #print('Adding P1 state')
                            statesP1.append(nextBoard)
                            utilsP1.append(CalcUtil(nextBoard))
                            eVals[i] = utilsP1[-1]
                            
                            idealMoveP1.append(0)
                            #Up1.append(0)
                    UstarP2 = max(eVals)
                    idealMoveNum = eVals.index(max(eVals))
                    idealMoveP2[stateP2Num] = [rowMoves[idealMoveNum],colMoves[idealMoveNum]]
                    utilsP2[stateP2Num] = gamma * UstarP2
                else:
                    idealMoveP2[stateP2Num] = None
                    if winner == 1:
                        utilsP2[stateP2Num] = -1
                    else: #tie
                        utilsP2[stateP2Num] = 0 #-0.1
                      
        # Save new states
        statesP1 = np.asarray(statesP1)
        np.save('statesP1',statesP1)
        statesP2 = np.asarray(statesP2)
        np.save('statesP2',statesP2)
        
        # Save ideal moves
        idealMoveP1 = np.asarray(idealMoveP1)
        np.save('idealMoveP1',idealMoveP1)
        idealMoveP2 = np.asarray(idealMoveP2)
        np.save('idealMoveP2',idealMoveP2)
    except:
        print('ERROR')
"""
import numpy as np
statesP1 = list(np.load('statesP1.npy'))
statesP2 = list(np.load('statesP2.npy'))
idealMoveP1 = list(np.load('idealMoveP1.npy'))
idealMoveP2 = list(np.load('idealMoveP2.npy'))
"""
    
    
