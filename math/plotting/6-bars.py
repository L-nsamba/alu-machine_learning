#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']

plt.bar(people, fruit[0], color='red', width=0.5, label='apples')
plt.bar(people, fruit[1], color='yellow', width=0.5,
        bottom=fruit[0], label='bananas')
plt.bar(people, fruit[2], color='#ff8000', width=0.5,
        bottom=fruit[0] + fruit[1], label='oranges')
plt.bar(people, fruit[3], color='#ffe5b4', width=0.5,
        bottom=fruit[0] + fruit[1] + fruit[2], label='peaches')

plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()

plt.show()
