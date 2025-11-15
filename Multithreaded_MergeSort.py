import threading
import time

# Function for standard merge sort
def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function for merge operation in multithreaded merge sort
def merge(arr, left, mid, right):
    """Merge two halves of an array."""
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Function for multithreaded merge sort
def merge_sort_multithreaded(arr, left, right):
    """Sorts an array using the merge sort algorithm with multithreading."""
    if left < right:
        mid = (left + right) // 2

        # Create threads for the left and right halves
        left_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, left, mid))
        right_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, mid + 1, right))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        merge(arr, left, mid, right)

def main():
    # Input from user
    n = int(input("Enter the number of elements to sort: "))
    print("Enter the elements (space-separated):")
    arr = list(map(int, input().strip().split()))

    # Ensure the input size matches the specified number
    if len(arr) != n:
        print(f"Error: Expected {n} elements, but got {len(arr)}.")
        return

    # Copy the array for the different sorting methods
    arr_standard = arr.copy()
    arr_multithreaded = arr.copy()

    # Standard merge sort
    start_time = time.time()
    merge_sort(arr_standard)
    standard_time = time.time() - start_time
    print("\nSorted Array (Standard Merge Sort):")
    print(arr_standard)
    print(f"Time taken (Standard Merge Sort): {standard_time:.6f} seconds")

    # Multithreaded merge sort
    start_time = time.time()
    merge_sort_multithreaded(arr_multithreaded, 0, n - 1)
    multithreaded_time = time.time() - start_time
    print("\nSorted Array (Multithreaded Merge Sort):")
    print(arr_multithreaded)
    print(f"Time taken (Multithreaded Merge Sort): {multithreaded_time:.6f} seconds")

    # Performance analysis
    print("\nPerformance Analysis:")
    print("Best Case: O(n log n)")
    print("Worst Case: O(n log n)")

if __name__ == "__main__":
    main()
