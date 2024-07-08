import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from algorithms import *

def main():
    
    algorithm = input("Choose sorting algorithm (bubble, selection, insertion, merge, quick): ").strip().lower()
    data_size = int(input("Enter the number of elements to sort: ").strip())

    # Generate a list of random integers from 1 to 1000
    random_data = [random.randint(1, 1000) for _ in range(data_size)]

    # Select the sorting algorithm generator
    if algorithm == 'bubble':
        generator = bubble_sort(random_data.copy())
        title = "Bubble Sort"
    elif algorithm == 'selection':
        generator = selection_sort(random_data.copy())
        title = "Selection Sort"
    elif algorithm == 'insertion':
        generator = insertion_sort(random_data.copy())
        title = "Insertion Sort"
    elif algorithm == 'merge':
        generator = merge_sort(random_data.copy(), 0, len(random_data) - 1)
        title = "Merge Sort"
    elif algorithm == 'quick':
        generator = quick_sort(random_data.copy(), 0, len(random_data) - 1)
        title = "Quick Sort"
    else:
        print("Invalid algorithm choice")
        return

    # Initialize the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(1, data_size+1), random_data, color='skyblue')

    # Set titles and labels
    ax.set_title(title)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Record the start time
    start_time = [time.time()]

    # Function to update the bars
    def update(data, start):
        for bar, value in zip(bars, data):
            bar.set_height(value)
        elapsed_time = time.time() - start[0]
        text.set_text(f"Elapsed time: {elapsed_time:.4f} seconds")
        return bars

    ani = animation.FuncAnimation(fig, func=update, fargs=(start_time,), frames=generator, interval=1, repeat=False, blit=False)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
    