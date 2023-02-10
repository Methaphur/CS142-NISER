# Question 1. a) 
'''Given a list of size n consisting of consecutive 1s followed by consecutive 2s, find the
position of transition from 1 to 2 in O(log n) time.'''

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
print(list1)
print(transition(list1,0,len(list1)))
print()

# Question 1.b

'''Suppose you have a function F such that given two lists L1 and L2, f(L1, L2) returns the
difference of the sum of the elements of L1 and L2. Now given a list of size n that consists
of n - 1 many 1s and a single 2, find the position of 2 making at most 2 log n many calls
to the function F'''

def F(L1,L2):
  diff = 0 
  for x in L1: diff += x
  for y in L2: diff -= y
  return diff

def find_2(arr,left,right):
  # Making length of list even
  if len(arr)%2 != 0 :
    arr.append(1)
    right += 1
  
  # Traveresed through list and 2 not found
  if left > right:
    return False
  
  
  mid = (left+right)//2
  # Base condition 
  if arr[mid] == 2:
    return mid

  # Finding difference of left anf right halves
  left_list = arr[left:mid]
  right_list = arr[mid:right]
  diff = F(left_list,right_list)
  # if diff greater than zero , 2 is in left half else check right half
  if diff > 0:
    return find_2(arr,left,mid)
  return find_2(arr,mid,right)
 
print("Qs 1.b")
array = [1,1,1,2,1,1]
print(array)
print(find_2(array,0,len(array)))
print()

# Question 2.a
'''Given a list L and an integer N, write a code of merge sort to sort L that uses insertion
sort as the base case when the list is of size ≤ N.'''

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

'''Suppose there are n stairs. You are standing at the bottom (0th stair) and want to reach
the top. If you are at ith stair, you can climb either 1 stair or jump i stairs at a time.
How many ways you can reach the top?'''

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




# Question 3 : just search for kth element of 2 sorted lists on geeks for geeks
'''Given 2 sorted lists of size m and n Find the kth element in
O(log m + log n) time '''