import random
import time

# Helper function to choose the pivot as the median of three (first, middle, last elements)
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    values = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    values.sort()  # Sort the three elements by value
    return values[1][1]  # Return the index of the median value

# Insertion Sort for small subarrays
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Iterative Quicksort implementation
def iterative_quick_sort(arr):
    stack = []
    stack.append((0, len(arr) - 1))  # Push initial range to the stack

    while stack:
        low, high = stack.pop()  # Pop the range to process
        if low < high:
            # Partition step using the median of three pivot
            pivot_index = median_of_three(arr, low, high)
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]  # Swap pivot to the first element

            pivot = arr[low]
            i = low + 1
            for j in range(low + 1, high + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Swap pivot into correct position

            # Push the ranges of the subarrays to the stack
            stack.append((low, i - 2))  # Left subarray
            stack.append((i, high))     # Right subarray

# Timing function to measure sorting time
def time_sort(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start

# Empirical comparison on different input sizes and distributions
sizes = [100, 1000, 10000]
distributions = {
    "Random": lambda size: random.sample(range(size * 10), size),
    "Sorted": lambda size: list(range(size)),
    "Reverse Sorted": lambda size: list(range(size, 0, -1)),
    "Repeated": lambda size: [random.choice(range(10)) for _ in range(size)]
}

# Run comparisons and print results
for dist_name, dist_func in distributions.items():
    print(f"Testing on {dist_name} arrays")
    for size in sizes:
        arr = dist_func(size)
        print(f"\nSize: {size}")
        print(f"Iterative Quicksort: {time_sort(iterative_quick_sort, arr)} seconds")
    print("\n" + "="*40)
