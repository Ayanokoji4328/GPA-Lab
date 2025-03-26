import matplotlib.pyplot as plt

def draw_colored_shapes():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Draw and color a rectangle
    rectangle = plt.Rectangle((1, 1), 3, 2, color='lightblue', label="Rectangle")
    ax.add_patch(rectangle)
    
    # Draw and color a circle
    circle = plt.Circle((5, 5), 1.5, color='lightgreen', label="Circle")
    ax.add_patch(circle)
    
    # Draw and color a triangle
    triangle = plt.Polygon([[2, 6], [3, 8], [4, 6]], color='lightcoral', label="Triangle")
    ax.add_patch(triangle)
    
    # Draw and color a polygon
    polygon = plt.Polygon([[6, 1], [7, 2.5], [8, 1], [7, 0]], color='lightgoldenrodyellow', label="Polygon")
    ax.add_patch(polygon)
    
    # Configure plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    plt.title("Colored Shapes")
    plt.legend(loc="best")
    plt.show()

# Run the function to display colored shapes
draw_colored_shapes()
