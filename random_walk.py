# Random walk of a dot with circles
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


class Circle:
    def __init__(self, position):
        self.life = 0
        self.position = position

    def step_life(self):
        self.life = self.life + 1

    def get_life(self):
        return self.life

    def get_position(self):
        return self.position


def update(f):
    ax.cla()  # Clear ax
    set_axis()
    ax.text(xmin, ymax * 0.9, "Step=" + str(f))

    # Draw marker
    global pm, rm, stp, circles, max_num_circles
    marker = patches.Circle(xy=pm, radius=rm, color='red')
    ax.add_patch(marker)
    # Append circle
    circle = Circle(pm)
    circles.append(circle)
    if len(circles) > max_num_circles:
        del circles[0]
    # Draw circles
    for i in circles:
        pc = i.get_position()
        rc = (i.get_life() + 1) * stp
        c = patches.Circle(xy=pc, radius=rc, fill=False)
        ax.add_patch(c)
        i.step_life()
    # Next point of dot
    theta = np.random.rand() * math.pi * 2
    pm = [pm[0] + stp * math.cos(theta), pm[1] + stp * math.sin(theta)]
    # Reset point of marker if out out of range
    if (pm[0] > xmax or pm[0] < xmin) or (pm[1] > ymax or pm[1] < ymin):
        pm = [0., 0.]


def set_axis():
    ax.set_title("Random walk of a dot with circles")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("equal")
    ax.grid()


# Global variables
xmin = -10.
xmax = 10.
ymin = -10.
ymax = 10.
pm = np.array([0., 0.])     # Point of a marker
rm = 0.1  # Radius of a marker
stp = 0.5    # Step of marker motion
max_num_circles = 50

# List circles
circles = []

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
