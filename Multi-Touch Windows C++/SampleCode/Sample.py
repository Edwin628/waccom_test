import matplotlib.pyplot as plt
import numpy as np
def fun():
    x = np.arange(-5, 5, 0.02)
    y = np.sin(x)
    plt.axis([-np.pi, np.pi, -2, 2])
    plt.plot(x, y, color="r", linestyle="-", linewidth=1)
    plt.show()