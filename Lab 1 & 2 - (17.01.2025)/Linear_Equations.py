def solve_linear_equation(a1, b1, c1, a2, b2, c2):
    # Determinant of the coefficient matrix
    det_A = (a1 * b2 - a2 * b1)

    det_Ax = c1 * b2 - c2 * b1
    det_Ay = a1 * c2 - a2 * c1
    
    if det_A == det_Ax == det_Ay == 0:
        return "Infinite solutions exist."
    elif det_A == 0 and det_Ax !=0 or det_Ay != 0:
        return "No unique solution exists."
    
    x = det_Ax / det_A
    y = det_Ay / det_A
    
    return (f"The solution is x = {x}, y = {y}")


print("Enter the coefficients for the equations:")
print("Equation 1: a1 * x + b1 * y = c1")
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))
print("Equation 2: a2 * x + b2 * y = c2")
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))


result = solve_linear_equation(a1, b1, c1, a2, b2, c2)
print(result)
