import umap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assuming you have your high-dimensional data in 'data'
# Example: random data for demonstration
import numpy as np
data = np.random.rand(100, 5)  # 100 points, 5 dimensions

# Apply UMAP
umap_model = umap.UMAP(n_components=3)
embedding = umap_model.fit_transform(data)

# Plotting in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot in 3D
ax.scatter(embedding[:, 0], embedding[:, 1], embedding[:, 2], c='b', marker='o')

ax.set_xlabel('UMAP 1')
ax.set_ylabel('UMAP 2')
ax.set_zlabel('UMAP 3')
plt.show()

