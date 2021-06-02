import matplotlib.pyplot as plt
import numpy as np

# Create a figure containing a single axes.
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # add data on the axes

# plotting without explicitly creating an axes
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Matplotlib plot X and Y
