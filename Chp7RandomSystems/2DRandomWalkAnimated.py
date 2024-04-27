# Just a single random walk this time, to better visualize the path as time continues.
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def main():
    #steps = int(input('How many steps do you want your walkers to take?  '))
    steps = 100
    x_vals = [0] # Array of x positions
    y_vals = [0] # Array of y positions
    x, y = 0, 0  # Starting position
    fig, ax = plt.subplots()
    arrow = ax.arrow(0,0,0,0) # Shows direction of walker
    for i in range(steps):
        arrow.remove()
        # 50% chance of moving forward once or back
        if random.random() < 0.5:
            x += 1
            dx = 0.01
        else:
            x -= 1
            dx = -0.01
        if random.random() < 0.5:
            y += 1
            dy = 0.01
        else:
            y -= 1
            dy = -0.01
        x_vals.append(x)
        y_vals.append(y)
        # Plot path and arrow
        ax.plot(x_vals, y_vals, color = 'b')
        arrow = ax.arrow(x, y, dx, dy, color = 'r', head_width = 1)
        # Set Dimensions of plot
        ax.set_xlim(-25, 25)  
        ax.set_ylim(-25, 25)  

        plt.pause(0.25)
    ax.plot(x_vals, y_vals, color = 'b')
    plt.show()

if __name__ == "__main__":
    main()