board=[['_','_','_'],['_','_','_'],['_','_','_']]

gameOver = False

def DisplayBoard():
    for i in board:
        print()
        for j in i:
            print(j,end=' ')
            
def Player1Input():
    row = input('Enter row no: ')
    column = input('Enter column no: ')
    
    try:
        board[int(row)-1][int(column)-1] = 'X'
    except:
        print('Invalid input!')
    
def Player2Input():
    row = input('Enter row no: ')
    column = input('Enter column no: ')
    
    try:
        board[int(row)-1][int(column)-1] = 'O'
    except:
        print('Invalid input!')
    
#FIXME: Referee does not know the rules of the game lol
def Referee():
    global gameOver
    #Checking if Player X won
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        print('Player X Wins')
        gameOver = True
        
    elif board[1][0] == board[1][1] == board[1][2] == 'X':
        print('Player X Wins')
        gameOver = True
        
    elif board[2][0] == board[2][1] == board[2][2] == 'X':
        print('Player X Wins')
        gameOver = True
        
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        print('Player X Wins')
        gameOver = True
        
    elif board[0][2] == board[1][1] == board[2][0] == 'X':
        print('Player X Wins')
        gameOver = True

    #Checking if player O wins
    elif board[0][0] == board[0][1] == board[0][2] == 'O':
        print('Player O Wins')
        gameOver = True
        
    elif board[1][0] == board[1][1] == board[1][2] == 'O':
        print('Player O Wins')
        gameOver = True
        
    elif board[2][0] == board[2][1] == board[2][2] == 'O':
        print('Player O Wins')
        gameOver = True
        
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        print('Player O Wins')
        gameOver = True
        
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        print('Player O Wins')
        gameOver = True
          
#FIXME: the game flow is a disaster
while gameOver==False:
    DisplayBoard()
    print()
    print()
    Player1Input()
    print()
    print()
    Referee()
    if gameOver == True:
        break
    DisplayBoard()
    print()
    print()
    Player2Input()
    if gameOver == True:
        break


#TODO:
#2 modes AI and Multiplayer Modes