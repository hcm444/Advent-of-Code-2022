<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
file = open('Day8.txt', 'r').readlines()
data = np.array([[int(x) for x in y.strip()] for y in file])
plt.imshow(data)
plt.xticks([])
plt.yticks([])
plt.show()
