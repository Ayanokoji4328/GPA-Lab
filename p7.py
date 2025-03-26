import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def bezier_curve(control_points, num_points=100):
    """ 
    Generate a Bézier curve using control points.
    :param control_points: List of control points (x, y).
    :param num_points: Number of points on the curve.
    :return: Curve points as a numpy array.
    """
    n = len(control_points) - 1  # Degree of the curve
    t = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))

    for i in range(n + 1):
        binomial_coeff = comb(n, i)
        term = binomial_coeff * ((1 - t) ** (n - i)) * (t ** i)
        curve += np.outer(term, control_points[i])

    return curve

def plot_curve(control_points, curve_points):
    """ 
    Plot the Bézier curve and its control points.
    :param control_points: Control points (x, y).
    :param curve_points: Points on the curve.
    """
    control_points = np.array(control_points)
    plt.figure(figsize=(8, 6))

    # Plot control points and polygon
    plt.plot(control_points[:, 0], control_points[:, 1], 'o--', label='Control Polygon', color='gray')

    # Plot Bézier curve
    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bézier Curve', color='blue')

    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define control points
control_points = [(0, 0), (1, 2), (3, 3), (4, 0)]

# Generate Bézier curve
curve_points = bezier_curve(control_points)

# Plot the curve
plot_curve(control_points, curve_points)
