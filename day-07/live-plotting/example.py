import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create a blank figure and axis
fig, ax = plt.subplots()
x_vals = []
y_vals = []
index = 0

# Function that updates the plot
def animate(i):
    global index
    x_vals.append(index)
    y_vals.append(random.randint(0, 10))  # Simulate data stream
    index += 1

    ax.clear()  # Clear old frame
    ax.plot(x_vals, y_vals, marker='o', linestyle='-')

    ax.set_title("Live Random Data Plot")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Value")
    ax.grid(True)

# Use FuncAnimation to repeatedly call animate()
ani = animation.FuncAnimation(fig, animate, interval=1000)  # 1000ms = 1s

plt.tight_layout()
plt.show()
