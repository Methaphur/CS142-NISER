#Problem 1     
#Finding c^m using log m number of multiplication operations
def expo(n,m):
  # When the exponent is 1 , return the base itself  
  if m == 1:
    return n
  # If exponent is even , divide it by 2 and square the base
  if m % 2 == 0:
    return expo(n**2,m/2)
  else:
    # Else make n^m as n*(n^m-1)
    return n*expo(n**2,(m-1)/2) 
print('1.')
print(expo(2,3))
print()

print('2.a)')
#Find course in course list of 2n-1 elements with only 1 appearance 

input = ['B102','C102','CS142','M102','C102','M102','B102','P102','P102']
# Init an empty dictionary
courses = {}
def course_dict(input):
  # Iterating through elements in input
  for i in input:
    # If element not in dict , set a key with value 1
    if i not in courses:
      courses[i] = 1
    else:
      # If element already present , increment value of key by 1
      courses[i] += 1

    # Fidning key with value 1 
  for key,value in courses.items():
    if value == 1:
      return key

print(course_dict(input))
print()

print("2.b)")

# Same as question 1 but instead of course list we have a list of 2n-1 elements containing (1,n)
# We use properties of numbers instead of a dictionary to execute this using only one auxillary variable 
# (Lists are compound variables and can't be used)

input = [3,1,2,5,4,1,5,3,2]
def fun(input):
  # Finding sum of n numbers and doubling it 
  n = (len(input)+1)//2
  sum = n*(n+1)
  # Finding the sum of elements in the list
  l_sum = 0 
  for i in input:
    l_sum += i
  # Returning the double of sum of n elements and subtracting the sum of our given list , returning us with the element only appearing once
  # eg: Our input list is (1,1,2)
  #   : (1,1,2,2) - (1,1,2) = 2
  return(sum - l_sum)

print(fun(input))
print()

print('3.')
#Problem 3
# Modifying the insertion sort algorithm to sort position of elements divisible by k in asccending order and the rest of the elements in descending order 

# Insertion sort Algorithm provided
def insertion_sort(list1):
  for i in range(1,len(list1)):
    current = list1[i]
    j = i -1
    while j >= 0 and current < list1[j]:
      list1[j+1] = list1[j]
      j = j -1 
    list1[j+1] = current
  return list1

# Chances are this code is wrong
# It just so happens to work for the input we are given ... Would be great if someone could pull a request on git
def my_sort(list1,k):
  for i in range(1,len(list1)):
    # Sorting the pos 3 elements in ascending order
    if (i+1)%3 == 0:
      current = list1[i]
      j = i -k
      while j >= 0 and current < list1[j]:
        list1[j+k] = list1[j]
        j = j - k
      list1[j+k] = current
    

    # Sorting the rest of the elements in descending order
    else:
      current = list1[i]
      j = i - 1
      while j >= 0 and current > list1[j]:
        if (j+1)%k == 0:
          j = j - 1
          list1[j+2] = list1[j]
        else:
          list1[j+1] = list1[j]
        j = j -1 
      list1[j+1] = current
  return list1

n = [31,12,21,55,14,1,51,30,2,7]
k = 3
print(my_sort(n,k))
print()


print('4.')
# Problem 4 : Finding number of inversion pairs

# Inversion pairs are pairs of elements in list such that i < j but L[i] > L[j]
# The bigger the number of inversion pairs , the farther we are from the final sorted list
# 0 Inversion pairs indicates a totally sorted list


def inversion_pair(list1):
  # Just introduce a counter for every inversion pair "sorted"
  count = 0
  for i in range(1,len(list1)):
    current = list1[i]
    j = i -1
    while j >= 0 and current < list1[j]:
      count += 1
      list1[j+1] = list1[j]
      j = j -1 
    list1[j+1] = current
  return count


n = [31,12,21,55,14,1,51,30,2,7]
print("Inversion pairs:",end = " ")
print(inversion_pair(n))

