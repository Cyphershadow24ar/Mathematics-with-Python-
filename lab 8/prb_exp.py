import numpy as np  # Import NumPy for matrix operations

def method(A, x0, tol=1e-6, max_iter=1000):
    """
    Implements the Rayleigh Power Method to find the dominant eigenvalue 
    and its corresponding eigenvector of a given square matrix A.

    Parameters:
    A (numpy array)     : Square matrix whose dominant eigenvalue is to be computed
    x0 (numpy array)    : Initial guess for the eigenvector
    tol (float)         : Convergence tolerance (default is 1e-6)
    max_iter (int)      : Maximum number of iterations (default is 1000)

    Returns:
    Prints the estimated dominant eigenvalue and eigenvector
    """

    # Step 1: Normalize the initial vector to avoid numerical instability
    x = x0 / np.linalg.norm(x0)  

    # Step 2: Initialize eigenvalue estimate to 0
    lambda_old = 0  

    # Step 3: Start iterative process
    for i in range(max_iter):
        # Step 4: Compute matrix-vector multiplication: Ax
        Ax = np.dot(A, x)  

        # Step 5: Compute Rayleigh Quotient (new eigenvalue estimate)
        lambda_new = np.dot(x.T, Ax) / np.dot(x.T, x)  

        # Step 6: Normalize the new eigenvector estimate
        x = Ax / np.linalg.norm(Ax)  

        # Step 7: Print current iteration and eigenvalue estimate
        print(f"Iteration {i+1}: λ = {lambda_new:.6f}")  

        # Step 8: Check for convergence
        if abs(lambda_new - lambda_old) < tol:
            break  # Stop iteration if the change in eigenvalue is within tolerance

        # Step 9: Update lambda_old for the next iteration
        lambda_old = lambda_new  

    # Step 10: Print final computed eigenvalue and eigenvector
    print("\nFinal Approximation:")
    print(f"Eigenvalue: {lambda_new:.6f}")  # Print dominant eigenvalue
    print(f"Eigenvector: {x}")  # Print corresponding eigenvector

# Define a square matrix A
A = np.array([[2, 1], 
            [3, 3]])

# Define an initial guess vector
x0 = np.array([1, 1])

# Call the function with the given matrix and initial vector
method(A, x0)
