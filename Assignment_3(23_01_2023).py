# Question 1 
# Evaluating a well defined expression using divide and conquer approach

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