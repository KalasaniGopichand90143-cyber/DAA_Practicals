import time

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Take user input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start execution time
start_time = time.perf_counter()

# Call Quick Sort
quick_sort(arr, 0, n - 1)

# End execution time
end_time = time.perf_counter()

# Display the sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {end_time - start_time:.10f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n²)")
print("Space Complexity:")
print("Best/Average : O(log n)")
print("Worst        : O(n)")