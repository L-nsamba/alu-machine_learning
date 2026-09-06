#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Graph 1
plt.subplot(3, 2, 1)
plt.plot(y0, color='red')
plt.xlabel('x', fontsize='x-small')
plt.ylabel('y', fontsize='x-small')
plt.title('y = x^3', fontsize='x-small')

# Graph 2
plt.subplot(3, 2, 2)
plt.scatter(x1, y1, color='magenta')
plt.xlabel('x', fontsize='x-small')
plt.ylabel('y', fontsize='x-small')
plt.title('Random Distribution', fontsize='x-small')

# Graph 3
plt.subplot(3, 2, 3)
plt.plot(x2, y2)
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.ylim()
plt.title('Exponential Decay of C-14', fontsize='x-small')
plt.yscale('log')

# Graph 4
plt.subplot(3, 2, 4)
plt.plot(x3, y31, color='red', linestyle='--', label='C-14')
plt.plot(x3, y32, color='green', linestyle='-', label='Ra-226')
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title('Exponential Decay of Radioactive Elements', fontsize='x-small')
plt.legend(loc='upper right', fontsize='small')

# Graph 5
plt.subplot(3, 1, 3)
plt.hist(student_grades)
plt.xlabel('Grade', fontsize='x-small')
plt.ylabel('Frequency', fontsize='x-small')
plt.title('Student Grades', fontsize='x-small')

plt.suptitle('All in One')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
