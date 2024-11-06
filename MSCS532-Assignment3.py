import random
import time
import copy

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Use the first element as the pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)
def run_experiment(sort_func, array):
    start_time = time.time()
    sort_func(copy.deepcopy(array))  # Use a copy to keep original array unchanged
    return time.time() - start_time

def generate_arrays(size):
    random_array = [random.randint(0, 100) for _ in range(size)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]
    repeated_elements_array = [random.choice([5, 10, 15]) for _ in range(size)]
    return random_array, sorted_array, reverse_sorted_array, repeated_elements_array

# Sizes for testing
sizes = [100, 500, 1000, 5000, 10000]
results = {}

for size in sizes:
    arrays = generate_arrays(size)
    results[size] = {
        "Random": arrays[0],
        "Sorted": arrays[1],
        "Reverse Sorted": arrays[2],
        "Repeated Elements": arrays[3]
    }
    print(f"\nSize: {size}")

    for array_type, array in results[size].items():
        det_time = run_experiment(deterministic_quicksort, array)
        rand_time = run_experiment(randomized_quicksort, array)
        print(f"{array_type} Array - Deterministic: {det_time:.5f} s, Randomized: {rand_time:.5f} s")
