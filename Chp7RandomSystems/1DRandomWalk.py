import random
import matplotlib.pyplot as plt
import numpy as np

# Does a single random walk with n number of steps and returns an array containing its position
# at each step and its squared displacement.
def rwalk(num_steps):
    x_vals = [0] # Array of x positions
    x = 0        # Starting position
    for i in range(num_steps):
        # 50% chance of moving forward once or back
        if random.random() < 0.5:
            x += 1
        else:
            x -= 1
        x_vals.append(x)
    return x_vals 

def main():
    num_walkers = int(input('How many walkers would you like to include?  '))
    steps = int(input('How many steps do you want your walkers to take?  '))
    steps_array = np.arange(steps+1)
    for i in range(1, num_walkers+1):
        x_array = rwalk(steps) 
        plt.plot(steps_array, x_array)
    plt.title('Random Walk in One Dimension')
    plt.xlabel('Step')
    plt.ylabel('Position')
    plt.show()

if __name__ == "__main__":
    main()