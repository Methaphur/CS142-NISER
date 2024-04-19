# Iterative binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Return False if element not in list
    return False

# Recursive binary search
def binarySearch(arr, target, left, right):
    # Return False when element not in list
    if left > right:
        return False
    # Finding mid index
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    # Searching in the right half
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, right)
    # Searching in the left half
    else:
        return binarySearch(arr, target, left, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(arr, target))
print(binarySearch(arr, target, 0, len(arr) - 1))
