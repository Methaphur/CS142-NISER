# Problem 1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_prime_sums(n):
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            count += 1
            print(f'{i}+{n-i}={n}')
    return count

max_count = 0
max_number = 0

for num in range(2, 1000, 2):
    count = count_prime_sums(num)
    if count > max_count:
        max_count = count
        max_number = num

print(f'Maximum number of prime sums is {max_count} for number {max_number}')
print(count_prime_sums(max_number))

# Problem 2
# Check if node exists with both children
def checkboth(node):
    if node is None:
        return False
    if node.left and node.right:
        return True
    return checkboth(node.left) or checkboth(node.right)
