import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define the function f (if needed)
# f = ... (you need to define f if you want to compute its partial derivatives)

# Compute partial derivatives of f (if f is defined)
# f_x = sp.diff(f, x)  # Partial derivative w.r.t x
# f_y = sp.diff(f, y)  # Partial derivative w.r.t y

# Define functions for Jacobian
f1 = y * x**2
f2 = x * sp.sin(y)

# Compute partial derivatives
f1_x = sp.diff(f1, x)  # ∂f1/∂x
f1_y = sp.diff(f1, y)  # ∂f1/∂y
f2_x = sp.diff(f2, x)  # ∂f2/∂x
f2_y = sp.diff(f2, y)  # ∂f2/∂y

# Construct Jacobian matrix
J = sp.Matrix([[f1_x, f1_y], [f2_x, f2_y]])

# Print results
print("Jacobian Matrix:")
sp.pprint(J)


