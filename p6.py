import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_object(ax, vertices, edges, color, label):
    for edge in edges:
        x = [vertices[edge[0], 0], vertices[edge[1], 0]]
        y = [vertices[edge[0], 1], vertices[edge[1], 1]]
        z = [vertices[edge[0], 2], vertices[edge[1], 2]]
        ax.plot(x, y, z, color=color, label=label if edge == edges[0] else "")

def translate(vertices, tx, ty, tz):
    translation_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = vertices_homogeneous @ translation_matrix.T
    return transformed_vertices[:, :3]

def scale(vertices, sx, sy, sz):
    scaling_matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = vertices_homogeneous @ scaling_matrix.T
    return transformed_vertices[:, :3]

def rotate_x(vertices, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = vertices_homogeneous @ rotation_matrix.T
    return transformed_vertices[:, :3]

def rotate_y(vertices, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = vertices_homogeneous @ rotation_matrix.T
    return transformed_vertices[:, :3]

def rotate_z(vertices, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = vertices_homogeneous @ rotation_matrix.T
    return transformed_vertices[:, :3]

# Example usage
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Bottom square
                     [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])  # Top square

edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # Bottom square
         (4, 5), (5, 6), (6, 7), (7, 4),  # Top square
         (0, 4), (1, 5), (2, 6), (3, 7)]  # Vertical edges

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot original object
plot_3d_object(ax, vertices, edges, 'blue', 'Original')

# Apply transformations
translated_vertices = translate(vertices, 2, 3, 4)
scaled_vertices = scale(vertices, 1.5, 1.5, 1.5)
rotated_vertices = rotate_y(vertices, 45)

# Plot transformed objects
plot_3d_object(ax, translated_vertices, edges, 'green', 'Translated')
plot_3d_object(ax, scaled_vertices, edges, 'red', 'Scaled')
plot_3d_object(ax, rotated_vertices, edges, 'orange', 'Rotated')

# Configure the 3D plot
ax.set_title("3D Transformations")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.legend()
plt.show()
