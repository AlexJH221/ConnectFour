#Connect 4 Game with Two Players
def createBoard():
    mat = []
    for r in range(0, 6):
        mat.append(list())
        for c in range(0, 7):
            mat[r].append(0)
    
    return mat

def printBoard(mat):
    for r in range(0, len(mat)):
        for c in range(0, len(mat[r])):
            print(mat[r][c], end='\t')
        print()

def openCol(mat, col):
    return mat[0][col] == 0

def placeOne(mat, col):
    for r in range(len(mat)-1, -1, -1):
        if mat[r][col] == 0:
            mat[r][col] = 1
            break

def placeTwo(mat, col):
    for r in range(len(mat)-1, -1, -1):
        if mat[r][col] == 0:
            mat[r][col] = 2
            break

def playerOneMove(mat):
    print('Player One\'s turn')
    col = int(input('Enter column to place token (0-6): '))
    if openCol(mat, col):
        placeOne(mat, col)
    else:
        playerOneMove(mat)
    print('\n\n')

def playerTwoMove(mat):
    print('Player Two\'s turn')
    col = int(input('Enter column to place token (0-6): '))
    if openCol(mat, col):
        placeTwo(mat, col)
    else:
        playerTwoMove(mat)
    print('\n\n')

def colWin(mat, num):
    for r in range(0, len(mat)):
        for c in range(0, len(mat[r])-3):
            if mat[r][c] == mat[r][c+1] == mat[r][c+2] == mat[r][c+3] == num:
                return True
    return False

def rowWin(mat, num):
    for r in range(0, len(mat)-3):
        for c in range(0, len(mat[r])):
            if mat[r][c] == mat[r+1][c] == mat[r+2][c] == mat[r+2][c] == num:
                return True
    return False

def rightDiagWin(mat, num):
    for r in range(3, len(mat)):
        for c in range(0, 4):
            if mat[r][c] == mat[r-1][c+1] == mat[r-2][c+2] == mat[r-3][c+3] == num:
                return True
    return False

def leftDiagWin(mat, num):
    for r in range(0, 3):
        for c in range(0, 4):
            if mat[r][c] == mat[r+1][c+1] == mat[r+2][c+2] == mat[r+3][r+3] == num:
                return True
    return False

def oneWon(mat):
    if colWin(mat, 1):
        return True
    elif rowWin(mat, 1):
        return True
    elif rightDiagWin(mat, 1):
        return True
    elif leftDiagWin(mat, 1):
        return True
    else:
        return False

def twoWon(mat):
    if colWin(mat, 2):
        return True
    elif rowWin(mat, 2):
        return True
    elif rightDiagWin(mat, 2):
        return True
    elif leftDiagWin(mat, 2):
        return True
    else:
        return False

def playGame():
    mat = createBoard()
    while True:
        printBoard(mat)
        playerOneMove(mat)
        if oneWon(mat):
            printBoard(mat)
            print('Player One has won!!!')
            break
        printBoard(mat)
        playerTwoMove(mat)
        if twoWon(mat):
            printBoard(mat)
            print('Player Two has won!!!')
            break
    

def main():
    play = input('Do you want to play Connect 4 (Y or N): ')
    if play == 'Y':
        playGame()
    elif play == 'N':
        print('Sorry! Hope you can play next time!')
    else:
        main()

main()