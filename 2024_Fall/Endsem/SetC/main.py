# Problem 1
# Given a list of n numbers, and an additional z
# Find numebr of triples (i,j,k) such that i < j < k and numbers[i] + numbers[j] + numbers[k] = z

def find_triples(numbers, z):
    n = len(numbers)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if numbers[i] + numbers[j] + numbers[k] == z:
                    count += 1
                    print(f'{numbers[i]}+{numbers[j]}+{numbers[k]}={z}')
    return count


# Test case
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = 12
print("Number of triples:", find_triples(numbers, z))

# Problem 2
# Function that checks if there exists a node with a single child

def checksingle(node):
    if node is None:
        return False

    if node.left is None and node.right is not None:
        return True

    if node.left is not None and node.right is None:
        return True

    return checksingle(node.left) or checksingle(node.right)
