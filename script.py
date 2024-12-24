board=[['_','_','_'],['_','_','_'],['_','_','_']]

gameOver = False

def DisplayBoard():
    for i in board:
        print()
        for j in i:
            print(j,end=' ')
            
def Player1Input():
    while True:
        print('Player X:')
        row = input('Enter row no: ')
        column = input('Enter column no: ')

        try:
            if board[int(row)-1][int(column)-1] == 'X' or board[int(row)-1][int(column)-1] == 'O':
                print('\n[REFEREE]: Postion already filled!\n')
            else:
                board[int(row)-1][int(column)-1] = 'X'
                break
        except:
                print('\n[REFEREE]: Invalid input!\n')


def Player2Input():
    while True:
        print('Player O:')
        row = input('Enter row no: ')
        column = input('Enter column no: ')

        try:
            if board[int(row)-1][int(column)-1] == 'X' or board[int(row)-1][int(column)-1] == 'O':
                print('\n[REFEREE]: Postion already filled!\n')
            else:
                board[int(row)-1][int(column)-1] = 'O'
                break
        except:
                print('\n[REFEREE]: Invalid input!\n')


def Referee():
    global gameOver

    for i in range(3):
        for j in ['X','O']:
            if board[i][0] == board[i][1] == board[i][2] == j:
                print('\n[REFEREE]: Player',j,'Wins!')
                gameOver = True
                return
                
            elif board[0][i] == board[1][i] == board[2][i] == j:
                print('\n[REFEREE]: Player',j,'Wins!')
                gameOver = True
                return

            elif board[0][0] == board[1][1] == board[2][2] == j:
                print('\n[REFEREE]: Player',j,'Wins!')
                gameOver = True
                return

            elif board[0][2] == board[1][1] == board[2][0] == j:
                print('\n[REFEREE]: Player',j,'Wins!')
                gameOver = True
                return

    empty_space = False
    for i in board:
        for j in i:
            if j == '_':
                empty_space =  True
                continue

    if empty_space == False:
                print('\n[REFEREE]: Game is a Draw!')
                gameOver = True


print('''

▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀
░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄
''')
while gameOver==False:
    DisplayBoard()
    print()
    print()
    Player1Input()
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
#2 modes AI and Multiplayer Modes
