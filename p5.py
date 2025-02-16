import numpy as np
import matplotlib.pyplot as plt

def plot_polygon(vertices, color, label):
    vertices = np.vstack([vertices, vertices[0]])  # Close the polygon
    plt.plot(vertices[:, 0], vertices[:, 1], color=color, label=label)

def translate(vertices, tx, ty):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])  # Homogeneous coordinates
    transformed_vertices = vertices_homogeneous @ translation_matrix.T
    return transformed_vertices[:, :2]

def scale(vertices, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])  # Homogeneous coordinates
    transformed_vertices = vertices_homogeneous @ scaling_matrix.T
    return transformed_vertices[:, :2]

def rotate(vertices, angle):
    rad = np.radians(angle)  # Corrected np.radius to np.radians
    rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])  # Homogeneous coordinates
    transformed_vertices = vertices_homogeneous @ rotation_matrix.T  # Corrected typo in variable name
    return transformed_vertices[:, :2]

def reflect(vertices, axis):
    if axis == "x":
        reflection_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis == "y":
        reflection_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Invalid axis for reflection. Use 'x' or 'y'.")
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])  # Homogeneous coordinates
    transformed_vertices = vertices_homogeneous @ reflection_matrix.T
    return transformed_vertices[:, :2]

# Define vertices
vertices = np.array([[1, 1], [3, 1], [2, 4]])

# Plot original polygon
plot_polygon(vertices, "blue", "Original")

# Apply transformations
translated = translate(vertices, 2, 3)
scaled = scale(vertices, 2, 2)
rotated = rotate(vertices, 45)
reflected = reflect(vertices, "x")

# Plot transformed polygons
plot_polygon(translated, "green", "Translated")
plot_polygon(scaled, "red", "Scaled")
plot_polygon(rotated, "orange", "Rotated")
plot_polygon(reflected, "purple", "Reflected")

# Add axes, grid, and labels
plt.axhline(0, color='black', linewidth=0.5)  # Fixed typo in color
plt.axvline(0, color='black', linewidth=0.5)  # Fixed typo in color
plt.legend(loc="best")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("2D Transformations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.show()
