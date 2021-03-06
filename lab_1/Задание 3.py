import numpy as np
import matplotlib.pyplot as plt
x = np.arange( -10 , 10  , 0.01  )
plt.plot(x, np.log((x**2+1)*np.e**(-np.fabs(x)/10),1+np.tan(1/(1+np.sin(x)**2))))
plt.grid(True)
plt.show()