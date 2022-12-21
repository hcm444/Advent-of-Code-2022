<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
file = open('Day8.txt', 'r').readlines()
data = np.array([[int(x) for x in y.strip()] for y in file])
plt.imshow(data)
plt.xticks([])
plt.yticks([])
plt.show()
=======
import matplotlib.pyplot as plt
import numpy as np

def show_heatmap(data):
    # Normalize the data to range between 0 and 1
    data = (data - np.min(data)) / (np.max(data) - np.min(data))

    # Create a colormap
    cmap = plt.get_cmap('jet')

    # Display the heatmap
    plt.imshow(data, cmap=cmap, interpolation='nearest')
    plt.show()

# Example data
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Display the heatmap
show_heatmap(data)
>>>>>>> origin/main
