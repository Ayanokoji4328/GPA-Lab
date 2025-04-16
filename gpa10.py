import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)

# Create a ball (circle)
ball, = ax.plot([], [], 'ro', markersize=10)

# Define keyframes (X positions)
keyframes = [1, 4, 7, 9]  # Keyframe positions
timestamps = [0, 10, 20, 30]  # Keyframe times

# Generate interpolated positions
frames = np.linspace(0, 30, 100)  # 100 frames in total
x_positions = np.interp(frames, timestamps, keyframes)  # Linear interpolation
y_positions = np.full_like(x_positions, 2)  # Ball stays at a fixed Y position

def update(frame):
    ball.set_data([x_positions[frame]], [y_positions[frame]])  # Fix: Pass lists
    return ball,

# Animate
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=50, blit=True)

plt.show()
