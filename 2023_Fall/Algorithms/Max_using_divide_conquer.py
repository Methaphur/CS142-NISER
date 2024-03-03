def max_find(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    left = max_find(arr[:mid])
    right = max_find(arr[mid:])
    if left > right:
        return left
    return right


print(max_find([12,3,16,7,3,19]))