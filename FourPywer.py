board = [
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
    ['|','-','|','-','|','-','|','-','|','-','|','-','|','-','|','-','|'],
    ['|','1','|','2','|','3','|','4','|','5','|','6','|','7','|','8','|'],
    
]


def printBoard():
    for raw in board:
        print("")
        for col in raw:
            print(col, end="")
    print("\n")

def lowCaseAvalable(y,x):
    #verify what is the lower case where you can put the mark
    for raw in board:
        print('raw:',raw)
    return y,x

def selecCol(nb, mark):
    if(nb == 1):
        board[lowCaseAvalable(1,1)[0]][lowCaseAvalable(1,1)[1]] = 'o' #PBM: l'appel de la fonction LowCase se fait 2 fois donc jamais avec les memes x et y
    if(nb == 2):
        board[lowCaseAvalable(1,3)[0]][lowCaseAvalable(1,3)[1]] = 'o'
    if(nb == 3):
        board[lowCaseAvalable(1,5)[0]][lowCaseAvalable(1,5)[1]] = 'o'
    if(nb == 4):
        board[lowCaseAvalable(1,7)[0]][lowCaseAvalable(1,7)[1]] = 'o'
    if(nb == 5):
        board[lowCaseAvalable(1,9)[0]][lowCaseAvalable(1,9)[1]] = 'o'
    if(nb == 6):
        board[lowCaseAvalable(1,11)[0]][lowCaseAvalable(1,11)[1]] = 'o'
    if(nb == 7):
        board[lowCaseAvalable(1,13)[0]][lowCaseAvalable(1,13)[1]] = 'o'
    if(nb == 8):
        board[lowCaseAvalable(1,15)[0]][lowCaseAvalable(1,15)[1]] = 'o'

def main():
    # board[0][3] = 'O'
    mark = 'o'

    selecCol(1, mark)
    
    
    printBoard()



main()