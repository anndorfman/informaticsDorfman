import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
plt.plot(x, x**2-x-6, x, 0*x)
plt.grid(True)
plt.show()
