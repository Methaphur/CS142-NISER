# Question 1. a) 
def transition(arr,left,right):
    # List has been traversed through and no such transition exists
    if left >= right:
        return False
    
    # if mid element is 2 and prev element is 1 , transition occured 
    mid = (left + right)//2
    if arr[mid] == 2:
        if arr[mid-1] == 1:
            return mid
        else:
            # Call the function again on left part of list
            return transition(arr,left,mid-1)
    else:
        # call the function on right part of the list
        return transition(arr,mid+1,right)

list1 = [1,1,1,2,2,2,2]
print("Qs 1.a")
print(transition(list1,0,len(list1)))
print()

# Question 2.a

def my_sort(arr,N):
    # if list size is less than N : Call insertion_sort on list
    if len(arr) < N:
        return insertion_sort(arr)
    else:
    # Else call merge sort on list
        return merge_sort(arr)
    
def insertion_sort(arr):
  for i in range(1,len(arr)):
    current = arr[i]
    j = i -1
    while j >= 0 and current < arr[j]:
      arr[j+1] = arr[j]
      j = j -1 
    arr[j+1] = current
  return arr

def merge_sort(input_list):
  if len(input_list) == 1:
    return input_list
  
  mid = len(input_list)//2
  left_list = my_sort(input_list[:mid],len(input_list[:mid]))
  right_list = my_sort(input_list[mid:],len(input_list[mid:]))
  return merge(left_list,right_list)

def merge(left,right):
  Li = []
  while left and right:
    if left[0] < right[0]:
      a = left.pop(0) 
    else:
      a = right.pop(0)
    Li.append(a)
  if not left:
    Li = Li + right
  else:
    Li = Li + left
  return Li

list1 = [1,5,3,2,18,6,14,9]
N = 5
print("Qs 2.a")
print(my_sort(list1,N))
print()

# Question 2.b)
# Jump one stair at a time or i steps when on ith step
# f(n) = f(n-1)           n is odd
# f(n) = f(n-1) + f(n/2)  n is even

def count_way(n):
  if n <= 2:  # Init base condition for step 1 and 2 
    return 1

  if n % 2 != 0:  
    return count_way(n-1) 
  else:
    return count_way(n-1) + count_way(n/2)
n = 8
print("Qs 2.b")
print(count_way(n))

# To complete the function in O(n) time , we are expected to use Memorization (DP)
def opt_count_way(n):
  count = [0]*n  # Init a memory list with n zeroes
  count[0] , count [1] = 1,1   # Setting base case for step 1 and 2 as 1
  def count_ways(n,count):
    # f(n) = f(n-1)  n is odd
    if n % 2 != 0:
      if count[n-1] == 0: # nth element is not calculated
        count[n-1] = count_ways(n-1,count)
      return count[n-1]

    # f(n) = f(n-1) + f(n/2)
    else:
      if count[n-1] == 0: 
        count[n-1] = count_ways(n-1,count) + count_ways(n//2,count)
      return count[n-1]
  return count_ways(n,count)
print(opt_count_way(n))



# Question 3 : just search for kth element of 2 sorted lists on geeks for geeks
# Babunga code too lazy to comment/type
