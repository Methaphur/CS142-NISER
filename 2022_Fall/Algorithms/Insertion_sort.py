# Insertion sort Algorithm
def insertion_sort(arr):
  for i in range(1,len(arr)):
    current = arr[i]
    j = i -1
    while j >= 0 and current < arr[j]:
      arr[j+1] = arr[j]
      j = j -1 
    arr[j+1] = current
  return arr


# Insertion Sort Algorithm using Recursion
def recursive_sort(arr):
    if (len(arr)<=1):
        return arr
    else:
        a1=recursive_sort(arr[:len(arr)-1])
        current=arr[len(arr)-1]
        a1.append(current)
        j=len(a1)-2
        while (j>=0) and (current<a1[j]):
            a1[j+1]=a1[j]
            j=j-1
        a1[j+1]=current
        return a1

n = [1,6,3,21,17,19,34]
print(insertion_sort(n))
print(recursive_sort(n))