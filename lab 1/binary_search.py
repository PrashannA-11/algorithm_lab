import time
import random
import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def benchmark_binary_search():
    # Using larger sizes since binary search is more efficient
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
             20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
             200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    times = []

    for size in sizes:
        # Create sorted array (required for binary search)
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[-1]  # Worst-case scenario
        
        # Run multiple trials to get more stable measurements
        num_trials = 100
        total_time = 0
        
        for _ in range(num_trials):
            start_time = time.perf_counter()
            binary_search(arr, target)
            end_time = time.perf_counter()
            total_time += end_time - start_time
        
        times.append(total_time / num_trials)

    # Create theoretical O(log n) curve
    # Use log2 since binary search divides by 2 at each step
    theoretical_times = [np.log2(size) for size in sizes]
    
    # Scale theoretical curve to match actual data magnitude
    theoretical_scale = np.mean(times) / np.mean(theoretical_times)
    theoretical_times = [t * theoretical_scale for t in theoretical_times]

    # Plotting
    plt.figure(figsize=(12, 7))
    
    # Plot actual benchmark results
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', 
             label='Actual Performance')
    
    # Plot theoretical O(log n)
    plt.plot(sizes, theoretical_times, linestyle='--', color='r', 
             label='Theoretical O(log n)')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Binary Search: Actual vs Theoretical Performance')
    plt.grid(True)
    plt.legend()
    
    # Add text explanation
    plt.figtext(0.99, 0.01, 
                'Note: Theoretical O(log n) curve is scaled to match actual data magnitude\n' +
                'Each data point is averaged over 100 trials',
                ha='right', fontsize=8, style='italic')
    
    # Add second subplot showing same data with logarithmic x-axis
    plt.figure(figsize=(12, 7))
    
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', 
             label='Actual Performance')
    plt.plot(sizes, theoretical_times, linestyle='--', color='r', 
             label='Theoretical O(log n)')
    
    plt.xscale('log')
    plt.xlabel('Input Size (n) - Log Scale')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Binary Search: Actual vs Theoretical Performance (Log Scale)')
    plt.grid(True)
    plt.legend()
    
    plt.figtext(0.99, 0.01, 
                'Note: X-axis is logarithmic to better visualize the logarithmic growth pattern',
                ha='right', fontsize=8, style='italic')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    benchmark_binary_search()