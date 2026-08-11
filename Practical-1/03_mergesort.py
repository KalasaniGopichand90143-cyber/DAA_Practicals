import time

# Merge function
def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

# Merge Sort function
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Take user input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start execution time
start_time = time.perf_counter()

# Call Merge Sort
merge_sort(arr, 0, n - 1)

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
print("Worst Case   : O(n log n)")
print("Space Complexity: O(n)")