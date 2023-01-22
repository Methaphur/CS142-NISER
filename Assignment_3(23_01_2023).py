# # Question 1 
# # Evaluating a well defined expression using divide and conquer approach
# # Analyze the time complexity of your program (:copium:)

# print("Qs 1.")
# list1 = ['(','(',3,'+',2,')','-','(','(',1,'-',2,')','+',5,')',')']

# def operation(n1,n2,operator):
#     if operator == "+":
#         return n1 + n2 
#     if operator == "-":
#         return n1 - n2

# def index_find(arr,char):
#     for index in range(len(arr)):
#         if arr[index] == char:
#             return index

# def evaluate(arr):
#     # Base condition 
#     if len(arr) == 1:
#         return arr[0]
    
#     # Recursive function
#     br = index_find(arr,")")
#     left = evaluate(arr[:br+1])
#     right = evaluate(arr[br+1:])
#     return merge(left,right)

# def compute(arr):
#     if len(arr) == 1:
#         return arr
    
#     i = index_find(arr,")")
#     result = operation(arr[i-3],arr[i-1],arr[i-2])
#     arr[i] = result
#     del arr[i-4:i]
#     return compute(arr)

# def merge(left,right):
#     Li = []
#     Li += compute(left)
#     Li += compute(right)
#     return Li

# print(evaluate(list1))


# def princ_op(inlist):
# 	i=0
# 	j=0
# 	if len(inlist)==9:
# 		new=[2,len(inlist)-3]
# 		for m in new:
# 			if inlist[m]=="+" or inlist[m]=="-":
# 				return m
# 	for k in range(1,len(inlist)-1):
# 		if inlist[k]=="(":
# 			i=i+1
# 		if inlist[k]==")":
# 			j=j+1
# 		if i==j:
# 			return k+1
	
# list1=['(','(',3,'+',2,')','-','(','(',1,'-',2,')','+',5,')',')']
# def compute(inlist):
# 	if len(inlist)==1:
# 		return int(inlist[0])
# 	if len(inlist)==5:
# 		if inlist[2]=="+":
# 			return int(inlist[1])+int(inlist[3])
# 		if inlist[2]=="-":
# 			return int(inlist[1])-int(inlist[3])
# 	else:
# 		i=princ_op(inlist)
# 		return compute(['(']+[compute(inlist[1:i])]+[inlist[i]]+[compute(inlist[i+1:len(inlist)-1])]+[')'])
	
# print(compute(list1))


def merge_sort(input_list):
  if len(input_list) == 1:
    return input_list
  
  mid = len(input_list)//2
  left_list = merge_sort(input_list[:mid])
  right_list = merge_sort(input_list[mid:])
  return merge(left_list,right_list)

def merge(left,right,count=0):
  Li = [] 
#   count = 0
  while left and right:
    if left[0] < right[0]:
      count += 1
      a = left.pop(0) 
    else:
      a = right.pop(0)
    Li.append(a) 
  if not left:
    Li = Li + right
  else:
    Li = Li + left
  return Li,count 


n = [31,12,21,55,14,1,51,30,2,7]
print(merge_sort(n))
