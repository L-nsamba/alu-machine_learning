#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color='red', linestyle='-')
plt.xlim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^3')
plt.show()
