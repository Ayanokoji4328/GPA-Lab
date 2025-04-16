import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define cube vertices
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])

# Define cube faces by vertex indices
faces_indices = [
    [0, 1, 2, 3], [4, 5, 6, 7],
    [0, 1, 5, 4], [2, 3, 7, 6],
    [1, 2, 6, 5], [4, 7, 3, 0]
]

# Set up figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

# Define rotation matrix around Z-axis
def rotate_z(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

# Define colors for faces
colors = ['cyan', 'magenta', 'yellow', 'red', 'green', 'blue']

# Update function for animation
def update(frame):
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_box_aspect([1, 1, 1])
    
    # Rotate vertices
    rotated_vertices = np.dot(vertices, rotate_z(frame * 0.1).T)
    
    # Create new rotated faces
    new_faces = [[rotated_vertices[j] for j in face] for face in faces_indices]
    
    # Change face colors dynamically
    face_colors = [colors[(frame // 10 + i) % len(colors)] for i in range(len(faces_indices))]
    
    # Draw faces
    for i, face in enumerate(new_faces):
        ax.add_collection3d(Poly3DCollection([face], facecolors=face_colors[i],
                                             edgecolors='k', alpha=0.6))

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
