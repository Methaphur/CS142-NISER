# Added a knight condition to N Queen problem 

import time 
def generate_board(N):
    board = [[0 for i in range(N)] for i in range(N)]
    return board

def print_board(board):
    pieces = {0:" ", 1:"Q" } 
    print('   ',end= "")
    print(*[i for i in range(len(board))],sep = "  ")
    i = 0
    for row in board:
        print("{:2}".format(i),end = " ")
        for item in row:
            print(f"|{pieces[item]}|",end = "")
            # print(f"|{item}|",end = "")
        print()
        i += 1
    print()

def has_queen(row,column,board):
    if board[row][column] == 1:
        return True
    else:
        return False

def valid_spot(row,column,board):

    # Row condition
    for i in range(len(board)):
        if board[i][column] == 1:
            return False

    # Column condition
    for col in range(len(board)):
        if board[row][col] == 1:
            return False
     
    # Left diagonal up  condition
    rows , col = row,column
    while rows >= 0 and col >= 0:
        if board[rows][col] == 1:
            return False
        rows -= 1
        col  -= 1

    # Left diagonal down  condition
    rows , col = row,column
    while rows < len(board) and col >= 0:
        if board[rows][col] == 1:
            return False
        rows += 1
        col  -= 1

    # Right diagonal up condition
    rows , col = row , column
    while rows >= 0 and col < len(board):
        if board[rows][col] == 1:
            return False
        rows -= 1
        col += 1

   # Right diagonal down condition
    rows , col = row , column
    while rows < len(board) and col < len(board):
        if board[rows][col] == 1:
            return False
        rows += 1
        col += 1

    # Knight condition 
    possible_moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for (x,y) in possible_moves:
        x = x + row
        y = y + column

        if x>= 0 and y>= 0 and x < len(board) and y < len(board):
            if board[x][y] == 1:
                return False

    return True


def max_queen(N):    
    if N <=3 :
        curr_max = 1
        board = generate_board(N)
        board[0][0] = 1
        return board,curr_max
    
    curr_max = 0
    out_board = []


    def queen_max(curr_row,board):
        nonlocal curr_max
        nonlocal out_board 

        if curr_max == N:   
            return 
        
        if curr_row == N:
            queen_count = count_queens(board)
            if queen_count > curr_max:
                curr_max = queen_count
                out_board = board
            return 
        
    
        configs = queen_configs(board,curr_row)    
        for curr_board in configs:
            queen_max(curr_row+1,curr_board)

    def queen_configs(board,current_row):
        configs = []

        for col in range(len(board)):
            temp_board = [sq.copy() for sq in board]
            if not has_queen(current_row,col,temp_board):
                if valid_spot(current_row,col,temp_board):
                    temp_board[current_row][col] = 1
                    configs.append(temp_board)

        if configs:
            return configs

        else:
            return [board]

    queen_max(0,generate_board(N))
    return out_board,curr_max

def count_queens(board):
    count = 0
    for row in board:
        for item in row:
            if item == 1:
                count += 1
    return count

n = int(input('NxN chess board: '))
start = time.time()
board,count = max_queen(n)
end = time.time()
print_board(board)
print(f'Max permissible Super Queens = {count}')
print(f'Time taken to execute : {end-start}')