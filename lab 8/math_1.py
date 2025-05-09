import sympy as sp       # Importing sympy as sp

x = sp.symbols('x')      # Defining x as a symbol

factored = sp.factor(x**2 - 2*x + 1)     # Factors to (x - 1)^2

solution = sp.solve(x**2 - 4, x)         # [-2, 2]

limit_value = sp.limit(sp.sin(x)/x, x, 0)  # 1

print(factored)
print("")
print(solution)
print("")
print(limit_value)

integral = sp.integrate(x**2, x)       # x^3/3

derivative = sp.diff(x**3 + 2*x, x)    # 3x^2 + 2

A = sp.Matrix([[sp.sin(x), 3], [sp.sin(x), 6]])

det_A = A.det()   # 3sin(x)

print(integral)
print("")
print(derivative)
print("")
print(A)
print("")
sp.pprint(A)  # Pretty print the matrix
print("")
print(det_A)

