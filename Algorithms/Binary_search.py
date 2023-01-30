# Return the index of target element in a sorted array
# left and right denote the indices of the start and end of algorithm
# Instead of slicing the list at mid interval, we are only computing to/from mid
def binary_search(arr,target,left,right):
    if left > right:
        return False
    else:
        mid = (left + right)//2        
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr,target,left,mid-1)
        else:
            return binary_search(arr,target,mid+1,right)
        
A = [1,3,5,6,8,10,11,13,14]
print(binary_search(A,5,0,len(A)))