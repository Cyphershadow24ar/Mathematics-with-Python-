def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    # Calculate the determinant of A
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return "The system of equations has no unique solution."

    # Calculate the inverse of A
    inverse_a = [
        [b2 / determinant, -b1 / determinant],
        [-a2 / determinant, a1 / determinant]
    ]

    # Multiply inverse(A) with B
    B = [c1, c2]
    x = inverse_a[0][0] * B[0] + inverse_a[0][1] * B[1]
    y = inverse_a[1][0] * B[0] + inverse_a[1][1] * B[1]

    return x, y

# User input for coefficients and constants
print("Enter coefficients and constants for the system of linear equations:")
print("Equation 1: a1*x + b1*y = c1")
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))

print("Equation 2: a2*x + b2*y = c2")
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

# Solve the equations
solution = solve_linear_equations(a1, b1, c1, a2, b2, c2)

# Display the solution
print("Solution:", solution)
