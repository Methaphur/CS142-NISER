# Problem 1

def mean_square(numbers):
    square_sum = 0
    for num in numbers:
        square_sum += num ** 2
    ms = (square_sum / len(numbers))
    return ms


def find_median(numbers):
    n = len(numbers)
    median_index = (n - 1) // 2
    pivot = numbers[0]
    smaller = [num for num in numbers if num < pivot]
    equal = [num for num in numbers if num == pivot]
    larger = [num for num in numbers if num > pivot]

    if median_index < len(smaller):
        return find_median(smaller)
    elif median_index < len(smaller) + len(equal):
        return equal[0]
    else:
        return find_median(larger)


numbers = [5, 6, 2, 8, 1, 9, 4, 6, 7, 3, 6]
rms = mean_square(numbers)
median = find_median(numbers)

print("Mean Square:", rms)
print("Median:", median)

# Problem 2
# Find the minimum value of all stored values in nodes in a given binary search tree
def find_min_bst(root):
    if root is None:
        return None
    if root.left is None:
        return root.value
    return find_min_bst(root.left)
