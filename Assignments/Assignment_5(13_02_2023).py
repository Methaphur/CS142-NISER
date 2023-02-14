# N Queen problem
def generate_board(N):
    # Generating a 2-D list with NxN elements
    # List comprehension  
    board = [[0 for i in range(N)] for i in range(N)]
    return board

def print_board(board):
    # Fancy way of printing the matrix
    pieces = {0 :" ", 1 :"Q"}     # 0s with spaces and 1s with Queen
    print('   ',end= "")
    print(*[i%10 for i in range(len(board))],sep = "  ") # printing top indices (just for reference)
    i = 0
    for row in board:
        print(i%10,end = " ") # printing vertical indices (just for reference)
        for item in row:
            print(f"|{pieces[item]}|",end = "")  #Printing |chess_piece|
            # print(f"|{item}|",end = "")
        print()
        i += 1
    print()


# Function to check if the current square has a queen
def has_queen(row,column,board):
    if board[row][column] == 1:
        return True
    else:
        return False

# Checking to see if the current spot conflicts with any of the already placed queens
def valid_spot(row,column,board):

    # Row condition
    for i in range(len(board)):
        if board[i][column] == 1:
            return False

    # Column condition
    for col in range(len(board)):
        if board[row][col] == 1:
            return False
     
    # The diagonal logic is just me using matrix logic
    # You can brute force it and check all the different indices 
    # Right diagonal condition
    rows , col = row,column
    while rows >= 0 and col >= 0:
        if board[rows][col] == 1:
            return False
        rows -= 1
        col  -= 1

    # Left diagonal condition
    rows , col = row , column
    while rows >= 0 and col < len(board):
        if board[rows][col] == 1:
            return False
        rows -= 1
        col += 1
    # If spot is not conlficting with any other spot return True
    return True


def n_queen(board,row):
    global count
    # Base condition: Queen has been placed in every row
    if row == len(board):
        # Print fancy board on finishing
        print_board(board)
        count += 1
        return None   

    # Going through every column in each row
    for col in range(len(board)):
        if not has_queen(row,col,board):
            if valid_spot(row,col,board):
                # If it's a valid spot , insert Queen there and move to next row
                board[row][col] = 1
                n_queen(board,row+1)
            board[row][col] = 0 # If not set that square as empty and move to next column

N = 5
count = 0
board = generate_board(N)    

n_queen(board,0)
print()
print(f'Count = {count}')