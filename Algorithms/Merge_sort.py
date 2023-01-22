def merge_sort(input_list):
  # Base condition
  if len(input_list) == 1:
    return input_list
  
  # Recursive algorithm
  mid = len(input_list)//2
  left_list = merge_sort(input_list[:mid])
  right_list = merge_sort(input_list[mid:])
  return merge(left_list,right_list)

# Merging algo
def merge(left,right):
  # Temp list
  Li = []
# While left and right has some elements
  while left and right:
    # Appending smaller element to temp list and removing it from parent list
    if left[0] < right[0]:
      a = left.pop(0)
    else:
      a = right.pop(0)
    Li.append(a)
  # If any of the list is empty , add the other list to Li 
  if not left:
    Li = Li + right
  else:
    Li = Li + left
  return Li

A = [3,2,7,1,5]
print(merge_sort(A))
