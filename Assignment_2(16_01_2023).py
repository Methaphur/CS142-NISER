# Question 1 : Evaluate the following commands
# In all the questions 'arr' refers to list 


print("Qs 1.")
list1 = ['(','(',3,'+',2,')','-','(','(',1,'-',2,')','+',5,')',')']
# For better visibility of the question ( not part of solution )
for i in list1:
    print(i,end = "")
print()



# Defining a function to compute an operation
def operation(n1,n2,operator):
  if operator == '+':
    return n1 + n2
  if operator == '-':
    return n1 - n2
    
# Defininf a function to return index of character in list 

def index_find(arr,char):
    for index in range(len(arr)):
        if arr[index] == char:
            return index

# Where the Actual magic happens
def fun(arr):
    # Defining Result condition 
    if len(arr) == 1:
      return arr[0]

    # Finding end of operation
    i = index_find(arr,")")
    # Calcualting operation using custom function
    result = operation(arr[i-3],arr[i-1],arr[i-2])
    # Replacing the ")" with computed result 
    arr[i] = result
    # Deleting "(" , n1 , n2 and the operator
    del arr[i-4:i]
    return fun(arr)
print(fun(list1))
print()

#Question 2:
# From a given list of n elements and target t , find elements a and b 
# such that a x b =  t . Algorithm must be in O(n) complexity 



# Approach 1 
# Using dictionary: Accessing elements from a dictionary has O(1) complexity 
# Python uses hash tables to work with dictionaries
def func(arr,t):
    hash = {}
    for i in range(len(arr)):
        var = t//arr[i]
        if var in hash:
            return f'{var} and {arr[i]}'
        hash[arr[i]] = 1

arr = [1, 5, 6, 8, 13, 17, 22, 45]
t = 132
print('Qs2. Approach 1')
print(arr,"target =",t)
print(func(arr,t))
print()
# Approach 2
# Traversing through the list once by going through elements from left and right
# Given our list is sorted
def fun2(arr,t):
  # Assigning indices of left most and right most elements 
  l = 0 
  r = len(arr)-1
  # Traversing through all the elements from both sides till they reach the center
  while l < r:
    # Target condition
    if arr[l] * arr[r] == t:
      return f'{arr[l]} and {arr[r]}'
    # If current product less than target: increase the lower bound 
    elif arr[l]*arr[r] < t:
      l += 1
    # Else decrease the upper bound 
    else:
      r -= 1

print('Qs2. Approach 2')
print(fun2(arr,132))
print()

# Given string S and an order O . Using the order O , sort the chars in S
# Modify Insertion sort
# Comparing values in insertion sort by comparing indices of those elements in Order O

def my_sort(string,O):
    # Converting string to list 
  list1 = list(string)
#   Insertion sort with modified condtion to compare 2 elements 
  for i in range(1,len(list1)):
    current = list1[i]
    j = i -1
    while j >= 0 and O.index(current) < O.index(list1[j]):
      list1[j+1] = list1[j]
      j = j -1
    list1[j+1] = current
    # Converting list to string
  string = ''
  for i in list1:
    string += i
  return string

S = 'dcabesfshdsakcdc'
O = 'bacdefshk'
print("Qs 3.")
print(my_sort(S,O))