# from tabulate import tabulate

# Generating the board
def generate_board(N):
    board = [[0 for i in range(N**2)] for i in range(N**2)]
    return board

# Function to ask user for input into the sudoku board
def user_inp(board):
    flag = True
    while flag:
        cord_input = input("Enter the cords: ")
        if cord_input != '':
            cord_input = cord_input.split(",")
            row , col = int(cord_input[0]) , int(cord_input[1])
            value = input("Enter pos value: ")
            board[row][col] = value
        else:
            flag = False
    pretty_print(board)

def board_init(board,input):
    for (row,col),value in input.items():
        board[row][col] = value 

# Printing using tabulate 
# def pretty_print(board):
#     visual_board = [row.copy() for row in board]
#     for row in range(len(board)):
#         for col in range(len(board)):
#             if visual_board[row][col] == 0:
#                 visual_board[row][col] = " "
#     print(tabulate(visual_board,tablefmt = "grid"))

def pretty_print(board):
    print(" " + "****"*len(board))
    for row in board:
        for item in row:
            if item == 0:
                item = " "
            print(f'| {item}' ,end = " ")
        print("|")
    print(" " + "****"*len(board))


def is_valid(board,row,col,num):
    for i in range(len(board)):
        # Row condition 
        if board[row][i] == num:
            return False
        
        # Column condition 
    for i in range(len(board)):
        if board[i][col] == num:
            return False

        # Sub matrix
    root_N = int((len(board))**0.5)
    x , y = (row - row%root_N) , (col - col%root_N)
    for i in range(x,x+root_N):
        for j in range(y,y+root_N):
            if board[i][j] == num:
                return False

    return True    
        

def available_spot(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return row,col       
    return False


def sudoku_solve(board):

    available_cords = available_spot(board)
    if not available_cords:
        return True

    row , col = available_cords

    for num in range(1,len(board)+1):
        if is_valid(board,row,col,num):
            board[row][col] = num
            # pretty_print(board)
            if sudoku_solve(board):
                return True

            board[row][col] = 0
    return 

# 
inp = {(0,6):2 , (1,1):8, (1,5):7, (1,7):9,
         (2,0):6 , (2,2):2, (2,6):5, (6,8):3,
         (3,1):7 , (3,4):6, (4,3):9, (4,5):1,
         (5,4):2 , (5,7):4, (6,2):5, (6,6):6,
         (7,1):9 , (7,3):4, (7,7):7, (8,2):6 }


board = generate_board(3)
board_init(board,inp)
import time 

pretty_print(board)
print()
start = time.time()
sudoku_solve(board)
end = time.time()
pretty_print(board)
print(f'Time taken to execute: {end-start}')