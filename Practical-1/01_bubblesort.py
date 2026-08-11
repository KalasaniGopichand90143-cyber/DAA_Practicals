import time

# Take user input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start execution time
start_time = time.perf_counter()

# Bubble Sort
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

# End execution time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")