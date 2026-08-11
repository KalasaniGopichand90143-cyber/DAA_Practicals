import time

# Take user input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start execution time
start_time = time.perf_counter()

# Selection Sort
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

# End execution time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

print(f"\nExecution Time: {end_time - start_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")