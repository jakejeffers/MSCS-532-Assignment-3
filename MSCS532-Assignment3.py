import random

def randomized_quicksort(arr):
    """Performs the randomized quicksort algorithm on the input array."""
    # Edge case: if the array has 0 or 1 elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Helper function to partition the array around a random pivot.
    def partition(arr, low, high):
        # Randomly select a pivot index and swap it with the last element.
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        
        # Partitioning logic
        i = low - 1  # This will be the "wall" position

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Move pivot to the correct location
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(arr, low, high):
        if low < high:
            # Get the pivot index after partitioning.
            pivot_index = partition(arr, low, high)
            # Recursively apply quicksort to the subarrays
            quicksort_recursive(arr, low, pivot_index - 1)
            quicksort_recursive(arr, pivot_index + 1, high)

    # Call the recursive quicksort function on the full array.
    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr  # The array is sorted in-place and returned.

# Example Usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quicksort(arr)
print("Sorted array:", sorted_arr)
