import sympy as sp

# Define the matrix
A = sp.Matrix([[22, 77, 11], 
            [33, 23, 89], 
            [55, 100, 100]])

# Compute the determinant
det_A = A.det()

# Print the determinant
print("Determinant of the matrix A is:", det_A)


