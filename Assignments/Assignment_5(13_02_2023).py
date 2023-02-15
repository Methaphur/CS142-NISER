#Problem 1:
'''Given a set of non-negative integers, a value t, and an integer k, determine
if there is a subset of size exactly k such that the sum of the elements in the set is equal to
t. Use backtracking to reduce the number of calls you make to your recursive function.'''

def subset_sum(arr, target, length):
    arr.sort() # Sorting the array so that weight gradually increases
    def is_subset_sum(current, weight, current_subset):
        # If sum has gone past the target element : skip
        if weight + arr[current] > target: 
            return False  
        
        # If the sum till current element is target 
        elif weight + arr[current] == target:
            # If the length of the subset is required length
            if len(current_subset) + 1 == length:   
                return True
            else:
                return False

        # Current has gone through all the elements in the list
        # Still no such sum pair has been found 
        if current == len(arr) - 1:
            return False
        
        else:
        # We call the subset function twice , once where we include the current element in the sum
        # And one where we exclude the current element in the sum
          include = is_subset_sum(current+1, weight + arr[current], current_subset + [arr[current]]) 
          exclude = is_subset_sum(current+1, weight, current_subset)

          return  include or exclude
    
    return is_subset_sum(0, 0, [])

print("Qs 1.a")
input = [3,34,4,5,12,5,2]
target = 9
length = 2
print(f'Input = {input} target = {target} length = {length}')
print(subset_sum(input,target,length))
print()
# Problem 1.b)
'''Given a set of positive and negative integers, and a value t, and an integer k determine
if there is a subset of size exactly k, such that the sum of the elements in the set is equal to
t. Write a program that uses the function in Problem 1 as a subroutine.'''

# We add a a positive number to all the list entries and update the target element correspondingly 
# Such a positive number is chosen so that all the negative elements in the list beome positive

def mod(x): # Completely redundant just use in-built abs() funtion
  if x < 0:
    return -x
  else:
    return x

def subset_sum(arr, target, length): 
    arr.sort()
    a = mod(min(arr))   # Finding mod of min list entry
    arr = [i+a for i in arr] # Adding that |min| to every element in list
    target = target + length*a  # Updating target to target + Length*|min|

    def is_subset_sum(current, weight, current_subset):
        if weight + arr[current] > target:
            return False  
        
        elif weight + arr[current] == target:
            if len(current_subset) + 1 == length:
                return True
            else:
                return False

        if current == len(arr) - 1:
            return False
        
        else:
          include = is_subset_sum(current+1, weight + arr[current], current_subset + [arr[current]]) 
          exclude = is_subset_sum(current+1, weight, current_subset)
          return  include or exclude
    
    return is_subset_sum(0, 0, [])

print("Qs 1.b")
input = [3,34,4,5,12,5,2,-3,-5,-4]
target = -12
length = 3
print(subset_sum(input,target,length))
print()
# Problem 2
# N Queen problem
'''Given an nxn chess board, you must place n queens on the board so that no
two queens attack each other. Print a matrix satisfying the conditions with positions with
queens marked with '1' and empty spaces with '0'. You must solve the n queens problem
using backtracking.
'''

def generate_board(N):
    # Generating a 2-D list with NxN elements
    # List comprehension  
    board = [[0 for i in range(N)] for i in range(N)]
    return board

def print_board(board):
    # Fancy way of printing the matrix
    pieces = {0 :" ", 1 :"Q"}     # 0s with spaces and 1s with Queen
    print('   ',end= "")
    print(*[i for i in range(len(board))],sep = "  ") # printing top indices (just for reference)
    i = 0
    for row in board:
        print(i,end = " ") # printing vertical indices (just for reference)
        for item in row:
            print(f"|{pieces[item]}|",end = "")  #Printing |chess_piece| (Qs and empty spaces) 
            # print(f"|{item}|",end = "")        # This line prints it as 0s and 1s in matrix
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

N = 8
count = 0
board = generate_board(N)    

n_queen(board,0)
print(f'Count = {count}')
print()

# Question 2.b)
# Added a knight condition to N Queen problem and minor code change 
# N Queen problem
# I'm not sure if the logic is correct for this one , pls feel free to pull request
def generate_board(N):
    board = [[0 for i in range(N)] for i in range(N)]
    return board

def print_board(board):
    pieces = {0:" ", 1:"Q" } 
    print('   ',end= "")
    print(*[i for i in range(len(board))],sep = "  ")
    i = 0
    for row in board:
        print(i,end = " ")
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

    # Knight condition 
    possible_moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for (x,y) in possible_moves:
        x = x + row
        y = y + column

        if x>= 0 and y>= 0 and x < len(board) and y < len(board):
            if board[x][y] == 1:
                return False

    return True

N = 8
board = generate_board(N)
def super_queen(board):
    count = 0
    max_queen = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if not has_queen(row,col,board):
                if valid_spot(row,col,board):
                    board[row][col] = 1
                    # print_board(board)
                    count += 1
        if max_queen < count:
            max_queen = count
    print_board(board)
    return max_queen

print("Qs 2.b)")
print("Super Queen")
print(f'Super Queen = {super_queen(board)}')



# Problem 3 
'''We have a function F such that
given two lists L1 and L2, f(L1, L2) returns the difference of the sum of the elements of L1
and L2. Now given a list of size 3k that consists of 3k - 1 many 1s and a single 2, 
find the position of 2 making at most k many calls to the function F. '''

def F(L1,L2):
    diff = 0
    for i in L1 : diff += i
    for j in L2 : diff -= j
    return diff

# Divide the list into three parts 
def find_2(arr,left,right):
    
    # Converting list to 3k form (not needed for our case where n = 3^k)
    if len(arr)%3 != 0:
        for i in range(3-len(arr)%3):
            arr.append(1)
    
    # Finding mid elements (Notion of distance)
    mid1 = left + (right-left)//3
    mid2 = mid1 + (right-left)//3
    
    if arr[left] == 2:
        return left

    elif arr[mid1] == 2:
        return mid1
    
    elif arr[mid2] == 2:
        return mid2

    # Slicing lists into left , mid and right lists
    left_list = arr[left:mid1]
    mid_list = arr[mid1:mid2] # Not really needed but just for symmetry
    right_list = arr[mid2:right]

    # Calling difference function on left and right list
    diff = F(left_list,right_list)

    # If difference is 0 , 2 is in mid list
    if diff  == 0:
        return find_2(arr,mid1,mid2)

    # If difference > 0 , 2 is in left list
    elif diff  > 0:
        return find_2(arr,left,mid1)
    
    # Else 2 in right list 
    else:
        return find_2(arr,mid2,right)

print("Qs 3.")
list1 = [1,1,1,2,1,1,1,1,1]
print(list1)
print(find_2(list1,0,len(list1)))
print()

# Question 4 
# Create a class in python
print("Qs 4.")
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def greetings(self):
        greeting = f'Hi! I am {self.name}'
        return greeting
    
    def birthday(self):
        self.age = self.age + 1
    
character_1 = Person("Methaphur",18)
print(character_1.age)
print(character_1.greetings())
character_1.birthday()
print(character_1.age)
