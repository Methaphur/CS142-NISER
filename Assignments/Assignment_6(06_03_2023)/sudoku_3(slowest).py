import time 
# Creating sudoku class
class Sudoku:
    def __init__(self):
        self.grid = dict()
        
#   Inserting given values
    def insert(self,values):
        for (x,y),value in values.items():
            self.grid[(x,y)] = value
          
#     Printing the board 
    def pretty_print(self):
        visual_board = [[" " for i in range(9)] for i in range(9)]
        for (x,y),value in self.grid.items():
            visual_board[x][y] = value

        print(" " + "****"*9)
        for row in visual_board:
            for item in row:
                print(f'| {item} ' , end = '')
            print('|')
        print(" " + "****"*9)

#       Finding next free square in board
    def available_spot(self):
        for row in range(9):
            for col in range(9):
                if (row,col) not in self.grid:
                    return row,col
        return False
    
#     Checking if a num can be placed in a given square in board
    def is_valid(self,row,col,num):

        for i in range(9):
            if (row,i) not in self.grid : continue
            if self.grid[(row,i)] == num:
                return False
        
        for i in range(9):
            if (i,col) not in self.grid : continue
            if self.grid[(i,col)] == num:
                return False
            
        x , y = (row - row%3) ,(col - col%3)
        for i in range(x,x+3):
            for j in range(y,y+3):
                if (i,j) not in self.grid : continue
                if self.grid[(i,j)] == num:
                    return False
        
        return True
#   Main function
    def solve(self):
        cords = self.available_spot()
        if not cords:
            return True

        row,col = cords

        for num in range(1,10):
            if self.is_valid(row,col,num):
                self.grid[(row,col)] = num
            
                if self.solve():
                    return True

                del self.grid[(row,col)]

        return False

# Inputting values into the sudoku board
inp =   {(0,6):2 , (1,1):8, (1,5):7, (1,7):9 ,
         (2,0):6 , (2,2):2, (2,6):5, (3,1):7 , 
         (3,4):6 , (4,3):9, (4,5):1, (6,8):3 ,
         (5,4):2 , (5,7):4, (6,2):5, (6,6):6 ,
         (7,1):9 , (7,3):4, (7,7):7, (8,2):6 }

sudoku = Sudoku()
sudoku.insert(inp)
sudoku.pretty_print()
print()
start = time.time()
sudoku.solve()
end = time.time()

sudoku.pretty_print()
print(f'Time taken to execute: {end-start}')
