import matplotlib.pyplot as plt
import numpy as np
def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], label = "Line")
def draw_rectangle(x, y, width, height):
    rectangle = plt.Rectangle((x, y), width, height, fill = False, label = "Rectangle")
    plt.gca().add_patch(rectangle)
def draw_circle(x, y, radius):
    circle = plt.Circle((x, y), radius, fill = False, label = "Circle")
    plt.gca().add_patch(circle)
def draw_polygon(vertices):
    polygon = plt.Polygon(vertices, fill = False, closed = True, label = "Polygon")
    plt.gca().add_patch(polygon)
def create_2d_objects():
    draw_line(0,0,5,5)
    draw_rectangle(1,1,4,2)
    draw_circle(3,3,2)
    vertices = [(2,5), (3,8), (5,7), (4,4)]
    draw_polygon(vertices)
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.axhline(0, color = 'black', linewidth = 0.5)
    plt.axvline(0, color = 'black', linewidth = 0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend(loc = "upper left")
    plt.title("2D Objects in Python")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
create_2d_objects()
