from matplotlib import pyplot as plt
import numpy as np 
def plot_equations():
    x = np.linspace(-10,10,400)
    y1 = (6-3*x)/2
    y2 = x - 4

    plt.plot(x, y1, label ="2x - 3y = 18")
    plt.plot(x, y2, label ="6y = x - 54")
    # plt.plot(x, y2, label ="x-y = 4")
    plt.axhline(0, color='black', linewidth = 0.5)
    plt.axvline(0, color ='black', linewidth = 0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

plot_equations()
