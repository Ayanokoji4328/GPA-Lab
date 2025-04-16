from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a red rectangle
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(100, 100)
    glVertex2f(300, 100)
    glVertex2f(300, 200)
    glVertex2f(100, 200)
    glEnd()

    # Draw a green triangle
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 250)
    glVertex2f(250, 350)
    glVertex2f(150, 350)
    glEnd()

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)      # White background
    gluOrtho2D(0, 500, 0, 500)   # Coordinate system

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Modelling and Rendering")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

main()
