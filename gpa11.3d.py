from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera setup
    gluLookAt(4, 4, 8, 0, 0, 0, 0, 1, 0)

    # Apply rotation
    glRotatef(angle, 1, 1, 0)

    # Red solid cube
    glColor3f(1, 0, 0)
    glutSolidCube(1.5)

    # Green wireframe cube, moved to the left and back
    glPushMatrix()
    glTranslatef(-2.5, 0, -2)
    glColor3f(0, 1, 0)
    glutWireCube(1.0)
    glPopMatrix()

    glutSwapBuffers()

def update(_):
    global angle
    angle = (angle + 1) % 360
    glutPostRedisplay()
    glutTimerFunc(33, update, 0)  # ~30 FPS

def init():
    glClearColor(1, 1, 1, 1)  # White background
    glEnable(GL_DEPTH_TEST)

    # Setup perspective
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 1, 100)

    # Switch back to modelview
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Modelling & Viewing")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()
