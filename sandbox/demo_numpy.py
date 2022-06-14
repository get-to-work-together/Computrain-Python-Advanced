import numpy as np

a = np.array([1,2,3,4,5,6,7])

print(type(a))
print(a)

print([1,2,3] * 2)
print(np.array([1,2,3]) * 2)

x = np.linspace(1, 10, 101)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()