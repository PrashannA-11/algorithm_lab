import random
import time
import numpy as np
import matplotlib.pyplot as plt
from quicksort import quicksort


def benchmark_quicksort():
    # Define input sizes for benchmarking
    sizes = [
        1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
        15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 
        55000, 60000, 65000, 70000, 75000, 80000, 82000, 100000
    ]
    
    # Store execution times
    times = []

    # Run benchmark for each size
    for size in sizes:
        # Generate random input data
        arr = random.sample(range(size * 10), size)
        
        # Measure time taken by quicksort
        start_time = time.perf_counter()
        quicksort(arr, 0, len(arr) - 1)
        end_time = time.perf_counter()
        
        # Append time to list
        times.append(end_time - start_time)

    # Calculate theoretical O(n log n) complexity
    theoretical_times = [size * np.log2(size) for size in sizes]
    theoretical_scale = np.mean(times) / np.mean(theoretical_times)
    theoretical_times = [t * theoretical_scale for t in theoretical_times]

    # Plot actual vs theoretical performance
    plt.figure(figsize=(12, 7))

    # Linear Plot
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', label='Actual Performance')
    plt.plot(sizes, theoretical_times, linestyle='--', color='r', label='Theoretical O(n log n)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quick Sort: Actual vs Theoretical Performance (Linear Scale)')
    plt.grid(True)
    plt.legend()

    # Log-Log Plot
    plt.subplot(1, 2, 2)
    plt.loglog(sizes, times, marker='o', linestyle='-', color='b', label='Actual Performance')
    plt.loglog(sizes, theoretical_times, linestyle='--', color='r', label='Theoretical O(n log n)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quick Sort: Actual vs Theoretical Performance (Log-Log Scale)')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.legend()

    # Add notes and save plot
    plt.figtext(
        0.99, 0.01, 
        'Note: Theoretical O(n log n) curve is scaled to match actual data magnitude',
        ha='right', fontsize=8, style='italic'
    )
    plt.tight_layout()
    plt.savefig('quicksort_benchmark.png')  # Save plot as an image
    plt.show()


# Run benchmark
benchmark_quicksort()
