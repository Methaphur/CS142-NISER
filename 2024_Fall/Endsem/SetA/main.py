# Problem 1

def root_mean_square(numbers):
    square_sum = 0
    for num in numbers:
        square_sum += num ** 2
    rms = (square_sum / len(numbers)) ** 0.5
    return rms


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
rms = root_mean_square(numbers)
median = find_median(numbers)

print("Root Mean Square:", rms)
print("Median:", median)

# Problem 2
# Find the minimum value of all stored values in nodes in a given binary search tree
def find_min_bst(root):
    if root is None:
        return None
    if root.left is None:
        return root.value
    return find_min_bst(root.left)
