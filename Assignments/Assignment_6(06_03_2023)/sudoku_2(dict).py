import time


# Inserting values into sudoku
def insert(grid, values):
    for (x, y), value in values.items():
        grid[(x, y)] = value


# Printing the board
def pretty_print(grid):
    visual_board = [[" " for i in range(9)] for i in range(9)]
    for (x, y), value in grid.items():
        visual_board[x][y] = value
    print(" " + "****" * 9)

    for row in visual_board:
        for item in row:
            print(f'| {item} ', end='')
        print('|')
    print(" " + "****" * 9)


# Finding next free spot in board
def available_spot(grid):
    for row in range(9):
        for col in range(9):
            if (row, col) not in grid:
                return row, col
    return False


#  Checking if a num can be placed in a square
def is_valid(grid, row, col, num):
    for i in range(9):
        if (row, i) not in grid: continue
        if grid[(row, i)] == num:
            return False

    for i in range(9):
        if (i, col) not in grid: continue
        if grid[(i, col)] == num:
            return False

    x, y = (row - row % 3), (col - col % 3)
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if (i, j) not in grid: continue
            if grid[(i, j)] == num:
                return False
    return True


#  Main function
def solve(grid):
    cords = available_spot(grid)
    if not cords:
        return True

    row, col = cords

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[(row, col)] = num
            if solve(grid):
                return True

            # Backtracking
            del grid[(row, col)]

    return False


# Input cords for values in sudoku board
inp = {(0, 6): 2, (1, 1): 8, (1, 5): 7, (1, 7): 9,
       (2, 0): 6, (2, 2): 2, (2, 6): 5, (3, 1): 7,
       (3, 4): 6, (4, 3): 9, (4, 5): 1, (6, 8): 3,
       (5, 4): 2, (5, 7): 4, (6, 2): 5, (6, 6): 6,
       (7, 1): 9, (7, 3): 4, (7, 7): 7, (8, 2): 6}

# Init sudoku board
board = dict()
insert(board, inp)
pretty_print(board)
# Solving
start = time.time()
solve(board)
end = time.time()
# Printing output 
pretty_print(board)
print(f'Time taken to execute: {end - start}')
