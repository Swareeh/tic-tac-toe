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
        if board[int(row)-1][int(column)-1] == 'X' or board[int(row)-1][int(column)-1] == 'O':
            print('Postion Already filled!')
        else:
            board[int(row)-1][int(column)-1] = 'X'
    except:
        print('Invalid input!')
    
def Player2Input():
    row = input('Enter row no: ')
    column = input('Enter column no: ')
    
    try:
        if board[int(row)-1][int(column)-1] == 'X' or board[int(row)-1][int(column)-1] == 'O':
            print('Postion Already filled!')
        else:
            board[int(row)-1][int(column)-1] = 'O'
    except:
        print('Invalid input!')

def Referee():
    global gameOver

    for i in range(3):
        for j in ['X','O']:
            if board[i][0] == board[i][1] == board[i][2] == j:
                print('Player',j,'Wins!')
                gameOver = True
                
            elif board[0][i] == board[1][i] == board[2][i] == j:
                print('Player',j,'Wins!')
                gameOver = True

            elif board[0][0] == board[1][1] == board[2][2] == j:
                print('Player',j,'Wins!')
                gameOver = True

            elif board[0][2] == board[1][1] == board[2][0] == j:
                print('Player',j,'Wins!')
                gameOver = True


#FIXME: Decision to make it a draw
    # empty_space = True
    # for i in board:
    #     for j in i:
    #         if j == '_':
    #             break



          
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
        DisplayBoard()
        break
    DisplayBoard()
    print()
    print()
    Player2Input()
    Referee()
    if gameOver == True:
        DisplayBoard()
        break


#TODO:
#Don't skip the players turn if the player provides a invalid spot/a spot that is already filled
#2 modes AI and Multiplayer Modes
