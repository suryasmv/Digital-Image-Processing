import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([
    [0, 1, 1, 3, 3],
    [7, 2, 5, 5, 7],
    [6, 3, 2, 1, 1],
    [1, 4, 4, 2, 1]
])

def histogram_equalization(matrix):
    hist, bins = np.histogram(matrix, bins=256, range=(0, 256))
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    equalized_matrix = np.interp(matrix, bins[:-1], cdf_normalized)
    return equalized_matrix

def plot_histogram(matrix, title, ax):
    ax.hist(matrix.flatten(), bins=20, alpha=0.7, color='blue', edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    ax.grid(True)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot original histogram
plot_histogram(matrix, "Matrix Before Equalization", axs[0])

# Perform histogram equalization and plot the equalized histogram
matrix_after = histogram_equalization(matrix)
plot_histogram(matrix_after, "Matrix After Equalization", axs[1])

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
