import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
y = np.sin(x)/(x + 1)

plt.plot(x, y, 'red')
plt.grid()
plt.show()
