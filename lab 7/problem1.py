import numpy as np
def method(A, x0, tol=1e-6, max_iter=100):
    x = x0 / np.linalg.norm(x0) 
    lambda_old = 0  

    for i in range(max_iter):
        Ax = np.dot(A, x)  
        lambda_new = np.dot(x.T, Ax) / np.dot(x.T, x)  
        
        x = Ax / np.linalg.norm(Ax)  

        print(f"Iteration {i+1}: λ = {lambda_new:.6f}")   
        if abs(lambda_new - lambda_old) < tol:
            break 
        lambda_old = lambda_new

    print("\nFinal Approximation:")
    print(f"Eigenvalue: {lambda_new:.6f}")
    print(f"Eigenvector: {x}")

A = np.array([[2, 1], #2*2 matrix
            [3, 3]])

x0 = np.array([1, 1]) # initial guess vector

method(A, x0)


