# Question 1 
# Evaluating a well defined expression using divide and conquer approach
print("Qs 1.")
list1=['(','(',3,'+',2,')','-','(','(',1,'-',2,')','+',5,')',')']
# Better visibility of the question 
print("".join([str(i)for i in list1]))

# Finding the operator that divides the whole expression into 2 expressions
def find_operator(arr):
  # Counting the number of "(" and ")" until that index
  # Whenever the count is equal we have arrived at our "operator"
  left = 0
  right = 0
  for i in range(1,len(arr)-1):
    if arr[i] == "(":
      left += 1
    if arr[i] == ")":
      right += 1
    if left == right:
      return i + 1
  # Condition where such an operator is not formed (eg : " 5)) ")
  return -1

# Defining an function to compute an operation
def operation(n1,n2,operator):
  if operator == "+":
    return n1 + n2
  if operator == "-":
    return n1 - n2

  # Where the Actual magic happens 
def evaluate(arr):
  # Base condition that gives the final answer
  if len(arr) == 1:
    return arr[0]
  # Basic computable opertion : 
  # eg: "(",3,"+",2,")" 
  if len(arr) == 5:
    result = operation(arr[1],arr[3],arr[2])
    return result
  
  # Finding the mid operartor
  i = find_operator(arr)
  if i == -1:
      return arr[0]
  else:  
    # Dividing the expression into left and right halves
    # Recursive functions
    left = evaluate(arr[1:i])
    right = evaluate(arr[i+1:-1])
    # Returning the values of left and right havles into an expression
    return evaluate(["(",left,arr[i],right,")"])

print(evaluate(list1))
print()
# Question 2
# Find number of inversion pairs using merge sort
# Just add a global counter variable 
count = 0
def merge_sort(input_list):
  if len(input_list) == 1:
    return input_list
  
  mid = len(input_list)//2
  left_list = merge_sort(input_list[:mid])
  right_list = merge_sort(input_list[mid:])
  return merge(left_list,right_list)

def merge(left,right):
  global count
  Li = []
  while left and right:
    if left[0] < right[0]:
      a = left.pop(0) 
    else:
      count += len(left)
      a = right.pop(0)
    Li.append(a)
    
  if not left:
    Li = Li + right
  else:
    Li = Li + left
  return Li

print("Qs 2.")
A = [8, 4, 2, 1]
print(merge_sort(A))
print(f'Number of inversion pairs:{count}')
print()


print("Qs 3.")
# Question 3 :
# Modifying insertion sort to improve number of comparisons
# Logic : Basic insertion sort algorithm but instead of looping through all the elements
# We find the  position to insert the current element in the left side of the "sorted" list
# Finding the position using binary search (divide and conquer approach)

def insertion_sort(arr):
  for i in range(1,len(arr)):
    current = arr[i]
    # Comapre is the alr sorted part of my list
    compare = arr[:i]
    # Returning the list with current element and the rest of the list
    arr = comparison(compare,current) + arr[i+1:]
  return arr


def comparison(arr,current):
  if len(arr) == 1:
    if arr[0] <  current:
        arr.insert(1,current)
        return arr
    else:
      arr.insert(0,current) 
      return arr
      
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  if right[0] > current:
    return comparison(left,current)+right
  else:
    return left+comparison(right,current) 

A = [21,3,4,16,8,1,17,2]
print(insertion_sort(A))
print()

print("Qs. 4")
# Find the median of 2 sorted lists when joined 

def median(arr1,arr2):
  # Base condition :
  if len(arr1) == 2:
    return f'{max(arr1[0], arr2[0])} and {min(arr1[1], arr2[1])}'
  
  # Checking mid element
  mid1 = len(arr1)//2
  mid2 = len(arr1)//2 + len(arr1)%2 - 1

  if arr1[mid1] == arr2[mid2]:
    return (arr1[mid1],arr1[mid1])
  # Dividing list by half and returning only median ranges significant
  elif arr1[mid1] < arr2[mid2]:
    return median(arr1[mid1:],arr2[:mid2+1])
  else:
    return median(arr1[:mid1+1],arr2[mid2:])

list1 = [3,5,6,7,9]
list2 = [5,8,9,11,23]
print(median(list1,list2))
