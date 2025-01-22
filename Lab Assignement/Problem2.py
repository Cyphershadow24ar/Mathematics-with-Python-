import numpy as np
import matplotlib.pyplot as plt

# Prompt the user for coefficients
print("For the first equation (a1*x + b1*y = c1):")
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

print("\nFor the second equation (a2*x + b2*y = c2):")
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

# Solve the system of equations using numpy
A = np.array([[a1, b1], [a2, b2]])  # Coefficient matrix
B = np.array([c1, c2])              # Constants matrix

try:
    solution = np.linalg.solve(A, B)
    x_sol, y_sol = solution
    print(f"\nThe solution is: x = {x_sol:.2f}, y = {y_sol:.2f}")

    # Graphical Representation
    x_vals = np.linspace(-10, 10, 400)  # X-axis range

    # Calculate y-values for each line
    y1_vals = (c1 - a1 * x_vals) / b1
    y2_vals = (c2 - a2 * x_vals) / b2

    # Plot the lines
    plt.plot(x_vals, y1_vals, label=f'{a1}x + {b1}y = {c1}')
    plt.plot(x_vals, y2_vals, label=f'{a2}x + {b2}y = {c2}')

    # Highlight the solution point
    plt.scatter(x_sol, y_sol, color='red', zorder=5, label=f'Solution: ({x_sol:.2f}, {y_sol:.2f})')

    # Add labels and legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Graphical Solution of Linear System')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

except np.linalg.LinAlgError:
    print("\nThe system of equations does not have a unique solution (may be inconsistent or dependent).")
