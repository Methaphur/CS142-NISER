# Problem 1 
def find_third_largest(lst):
    if len(lst) < 3:
        return "List should have at least 3 elements"
    
    first = second = third = lst[0]
    
    for num in lst:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num
    
    return third

print(find_third_largest([1, 2, 3, 4, 5]))

# Problem 2 
def findmax(root):
    if root is None:
        # Setting lowest possible value for None so that it can be compared with other values
        return float('-inf')
    
    result = root.value
    left = findmax(root.left)
    right = findmax(root.right)
    
    if left > result:
        result = left
    if right > result:
        result = right
    return result

