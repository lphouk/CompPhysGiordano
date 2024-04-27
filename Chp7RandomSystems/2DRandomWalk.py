import random
import matplotlib.pyplot as plt
import numpy as np

# Does a single random walk with n number of steps and returns an array containing its position
# at each step and its squared displacement.
def rwalk2D(num_steps):
    x_vals = [0] # Array of x positions
    y_vals = [0] # Array of y positions
    x,y = 0, 0   # Starting position
    for i in range(num_steps):
        # 50% chance of moving forward once or back
        if random.random() < 0.5:
            x += 1
        else:
            x -= 1
        if random.random() < 0.5:
            y += 1
        else:
            y -= 1
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

def main():
    num_walkers = int(input('How many walkers would you like to include?  '))
    steps = int(input('How many steps do you want your walkers to take?  '))
    for i in range(1, num_walkers+1):
        x_array, y_array = rwalk2D(steps) 
        plt.plot(x_array, y_array)
    plt.title('Random Walk in Two Dimensions')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.show()

if __name__ == "__main__":
    main()