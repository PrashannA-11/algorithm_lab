import time
import random
import matplotlib.pyplot as plt
import numpy as np

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def benchmark_linear_search():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
             15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 
             60000, 65000, 70000, 75000, 80000, 82000]
    times = []

    for size in sizes:
        arr = random.sample(range(size * 10), size)
        target = arr[-1]  # Worst-case scenario

        start_time = time.perf_counter()
        linear_search(arr, target)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    # Create theoretical O(n) curve
    # Scale the theoretical curve to match the actual data
    theoretical_scale = np.mean(times) / np.mean(sizes)  # Calculate scaling factor
    theoretical_times = [size * theoretical_scale for size in sizes]

    # Plotting
    plt.figure(figsize=(12, 7))
    
    # Plot actual benchmark results
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', label='Actual Performance')
    
    # Plot theoretical O(n)
    plt.plot(sizes, theoretical_times, linestyle='--', color='r', label='Theoretical O(n)')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Linear Search: Actual vs Theoretical Performance')
    plt.grid(True)
    plt.legend()
    
    # Add text explanation
    plt.figtext(0.99, 0.01, 
                'Note: Theoretical O(n) curve is scaled to match actual data magnitude',
                ha='right', fontsize=8, style='italic')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    benchmark_linear_search()