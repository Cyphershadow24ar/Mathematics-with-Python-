from matplotlib import pyplot as plt
import numpy as np
import math

def plot_and_calculate_angle():
    # User input for the coefficients of the linear equations
    print("Enter the coefficients for the equations in the form: Ax + By = C")
    
    # Equation 1: Ax + By = C -> y = (-A/B)x + (C/B)
    A1 = float(input("Enter A1 for the first equation (Ax + By = C): "))
    B1 = float(input("Enter B1 for the first equation (Ax + By = C): "))
    C1 = float(input("Enter C1 for the first equation (Ax + By = C): "))
    
    # Equation 2: Ax + By = C -> y = (-A/B)x + (C/B)
    A2 = float(input("Enter A2 for the second equation (Ax + By = C): "))
    B2 = float(input("Enter B2 for the second equation (Ax + By = C): "))
    C2 = float(input("Enter C2 for the second equation (Ax + By = C): "))
    
    # Calculate the slopes (m = -A/B)
    m1 = -A1 / B1
    m2 = -A2 / B2
    
    # Calculate the angle between the two lines using the formula
    angle_radians = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
    angle_degrees = math.degrees(angle_radians)
    print(f"The angle between the two lines is: {angle_degrees:.2f} degrees")
    
    # Generate x values for plotting
    x = np.linspace(-10, 10, 400)
    
    # Calculate the corresponding y values for both equations
    y1 = (-A1 * x + C1) / B1
    y2 = (-A2 * x + C2) / B2
    
    # Plot the lines
    plt.plot(x, y1, label=f"{A1}x + {B1}y = {C1}")
    plt.plot(x, y2, label=f"{A2}x + {B2}y = {C2}")
    
    # Draw the axes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Add grid and legend
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    
    # Display the plot
    plt.show()

# Call the function
plot_and_calculate_angle()
