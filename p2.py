import matplotlib.pyplot as plt

def draw_ellipse(a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    p1 = b2 - (a2 * b) + (0.25 * a2)
    dx = 2 * b2 * x
    dy = 2 * a2 * y
    points = []

    # Region 1
    while dx < dy:
        points.append((x, y))
        if p1 < 0:
            x += 1
            dx += 2 * b2
            p1 += dx + b2
        else:
            x += 1
            y -= 1
            dx += 2 * b2
            dy -= 2 * a2
            p1 += dx - dy + b2

    # Region 2
    p2 = (b2 * (x + 0.5) ** 2) + (a2 * (y - 1) ** 2) - (a2 * b2)
    while y >= 0:
        points.append((x, y))
        if p2 > 0:
            y -= 1
            dy -= 2 * a2
            p2 += a2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * b2
            dy -= 2 * a2
            p2 += dx - dy + a2

    return points

def plot_ellipse(a, b):
    ellipse_points = draw_ellipse(a, b)
    
    x_coords = []
    y_coords = []
    
    for x, y in ellipse_points:
        x_coords.extend([x, -x, x, -x])
        y_coords.extend([y, -y, -y, y])

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, 'bo', markersize=1)
    plt.title(f'Ellipse with a = {a}, b = {b}')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

plot_ellipse(100, 50)
