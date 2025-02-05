# Python program determines whether a given system of linear equations has a solution by computing 
# the rank of the coefficient matrix and the augmented matrix. 
# It also determines the type of solution (unique, infinite, or none) if a solution exists.

import copy
import numpy as np

def get_matrix(rows, cols):
    """Function to take user input for a matrix."""
    matrix = []
    print(f"Enter the {rows}x{cols} coefficient matrix (row-wise):")
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print("Error: Please enter exactly", cols, "values!")
            return get_matrix(rows, cols)  # Retry input
        matrix.append(row)
    return matrix

def get_constants(rows):
    """Function to take user input for constant matrix."""
    print(f"Enter the {rows}x1 constant matrix:")
    constants = list(map(float, input().split()))
    if len(constants) != rows:
        print("Error: Please enter exactly", rows, "values!")
        return get_constants(rows)  # Retry input
    return constants

# Taking user input
n = int(input("Enter the number of equations/variables: "))
A = get_matrix(n, n)
B = get_constants(n)

print("\nCoefficient matrix (A):", A)
print("Constant matrix (B):", B)

# Constructing the augmented matrix
AB = copy.deepcopy(A)
for i in range(n):
    AB[i].append(B[i])

print("\nAugmented Matrix (A|B):")
for row in AB:
    print(row)

# Compute ranks
ra = np.linalg.matrix_rank(A)
rab = np.linalg.matrix_rank(AB)
print("\nRank of coefficient matrix: ", ra)
print("Rank of augmented matrix: ", rab)

# Checking for solutions
if ra != rab:
    print("No solution exists!")
elif ra == rab == n:
    print("Unique solution exists!")
elif ra == rab < n:
    print("Infinite solutions exist!")
