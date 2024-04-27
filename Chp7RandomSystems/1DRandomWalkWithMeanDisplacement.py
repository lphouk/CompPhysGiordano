import random
import matplotlib.pyplot as plt
import numpy as np

# Does a single random walk with n number of steps and returns an array containing its position
# at each step and its squared displacement.
def rwalk(num_steps, num_walkers):
    steps_array = np.arange(num_steps+1)
    x2ave = [0] * (num_steps+1)
    # Generate a random walk for each walker
    for j in range(1, num_walkers+1): 
        x = 0        # Starting position
        x_vals = [0] # Array of x positions
        # Simulate a random walk
        for i in range(1, num_steps+1):
            # 50% chance of moving forward once or back
            if random.random() < 0.5:
                x += 1
            else:
                x -= 1
            x_vals.append(x)
            x2ave[i] += x**2
        # Plot the line onto the graph
        plt.plot(steps_array, x_vals)

    # Complete plot with labels
    plt.title('Random Walk in One Dimension')
    plt.xlabel('Step')
    plt.ylabel('Position')
    plt.show()

    # Normalize square displacements
    for elt in x2ave:
        elt /= num_walkers
    
    # Plot mean squared displacement against step
    plt.plot(steps_array, x2ave)
    plt.title('Random Walk in One Dimension')
    plt.xlabel('t (Step)')
    plt.ylabel('<x^2> (Mean Squared Displacement)')
    plt.show()
def main():
    num_walkers = int(input('How many walkers would you like to include? '))
    steps = int(input('How many steps do you want your walkers to take? '))
    rwalk(steps, num_walkers)
   
if __name__ == "__main__":
    main()