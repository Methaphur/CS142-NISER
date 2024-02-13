import random

# Function to initialize a matrix of size n x m with all elements as 0
def initializeMatrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix

# Function to initialize a matrix of size n x m with random elements
def randomMatrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(1, 10))
        matrix.append(row)
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def matrixMultiplication(matrix1, matrix2):
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])
    if m1 != n2:
        return "Invalid input"

    # Setting up a matrix of size n1 x m2 (size of matrix1 x matrix2)
    result = initializeMatrix(n1, m2)
    for i in range(n1):
        for j in range(m2):
            # Cij = \sigma_{k=1}^{m1} Aik * Bkj
            for k in range(m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

rows, cols = 3, 3

A = randomMatrix(rows, cols)
B = randomMatrix(rows, cols)
C = matrixMultiplication(A, B)
print("A",end="\n")
printMatrix(A)
print("B",end="\n")
printMatrix(B)
print("C",end="\n")
printMatrix(C)

# Using numpy ;)
import numpy as np
C = np.dot(A,B)
print(C)