import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys
import os


def main():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the limits of the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Create a point to animate
    point, = ax.plot([], [], 'ro')

    # Function to update the point's position
    def update(frame):
        x = frame * 0.1  # Move the point along the x-axis
        y = sp.sin(x) + 5  # Move the point along the y-axis using a sine function
        point.set_data(x, y)
        return point,

    # Create an animation
    ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True)

    # Show the animation
    plt.show()

