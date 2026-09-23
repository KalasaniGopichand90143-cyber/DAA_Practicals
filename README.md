# Practical 1 : Implementation and Time analysis of sorting algorithms. Bubble sort, Selection sort, Insertion sort, Merge sort and Quicksort

# Summary : 
In this practical, five fundamental sorting algorithms—Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort—were implemented and analyzed using Python. The execution time of each algorithm was measured to understand its practical performance. The algorithms were tested on input data and their time and space complexities were studied. Simple sorting algorithms such as Bubble, Selection, and Insertion Sort generally require O(n²) time in the average and worst cases, while Merge Sort and Quick Sort provide better average performance of O(n log n). This practical helped in understanding how different sorting techniques work and how their performance changes with the size and arrangement of input data.

# Conclusion:
The practical demonstrated that the choice of a sorting algorithm significantly affects program performance. Bubble Sort, Selection Sort, and Insertion Sort are simple and easy to implement, making them suitable for small datasets and learning purposes. However, their O(n²) average/worst-case time complexity makes them inefficient for large datasets. Merge Sort provides consistent O(n log n) performance, while Quick Sort generally performs very efficiently in practice with an average complexity of O(n log n), although its worst case can reach O(n²) depending on the pivot selection. Therefore, understanding the time and space complexity of sorting algorithms is essential for selecting an appropriate algorithm according to the size and nature of the input data



# Practical 2 : Implementation and Time analysis of linear and binary search algorithm

# Summary : 
In this practical, Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort were implemented using Python. The execution time of each sorting algorithm was measured using different input values. The practical helped to understand the working process, time complexity, and space complexity of each algorithm. Bubble, Selection, and Insertion Sort generally take O(n²) time, whereas Merge Sort and Quick Sort are more efficient for large datasets with an average time complexity of O(n log n).

# Conclusion : 
From this practical, we learned that different sorting algorithms have different performance levels. Bubble Sort, Selection Sort, and Insertion Sort are simple and suitable for small datasets, while Merge Sort and Quick Sort are more efficient for larger datasets. By analyzing execution time and time complexity, we can select the most suitable sorting algorithm according to the input size and requirements. Thus, this practical provided a clear understanding of the implementation, performance, and efficiency of sorting algorithms.


# Practical 3 : Implementation of max-heap sort algorithm


# Summary : 
In this practical, the Max-Heap Sort algorithm was implemented using Python. The practical focused on understanding the concept of a Max Heap, where the parent node is always greater than or equal to its child nodes. The heap was constructed by repeatedly applying the heapify operation, and the largest element was moved to its correct position during the sorting process. The implementation helped in understanding the working of heap-based sorting and its execution process. The time complexity of Heap Sort is O(n log n) in the best, average, and worst cases, while its space complexity is O(1) for an in-place implementation.

# Conclusion : 
The practical successfully demonstrated the implementation of the Max-Heap Sort algorithm and its use for sorting elements in ascending order. Heap Sort provides consistent O(n log n) performance regardless of the initial arrangement of the data. It is also memory-efficient because it can sort the elements in-place without requiring significant additional memory. Therefore, Max-Heap Sort is an efficient and reliable sorting technique, especially when predictable performance and low extra space usage are required performance and low extra space usage are required.



# Practical 4 : Implementation and Time analysis of factorial program using iterative and recursive method

# Summary : 

This practical implemented factorial using iterative and recursive methods in Python. The execution time of both methods was measured and compared. Both methods have O(n) time complexity, but they differ in space usage. The iterative method uses O(1) space, while the recursive method uses O(n) space.

# Conclusion : 
 
Both methods successfully calculate the factorial of a number. The iterative method is more memory-efficient, while the recursive method demonstrates the concept of recursion clearly. Therefore, iteration is preferred when memory efficiency is important.

# Practical 5 : Implementation of a knapsack problem using dynamic programming   

# Summary :

This practical implemented the 0/1 Knapsack Problem using Dynamic Programming. The algorithm determines the maximum value that can be placed in a knapsack without exceeding its capacity. Dynamic Programming stores solutions to smaller subproblems to avoid repeated calculations. The execution time and space requirements were also analyzed.

# Conclusion :

The Dynamic Programming approach efficiently solves the 0/1 Knapsack Problem and provides the optimal maximum value. It has a time complexity of O(n × capacity) and a space complexity of O(n × capacity). This practical demonstrates how Dynamic Programming can be used to solve optimization problems efficiently.



# Practical 6 : Implementation of chain matrix multiplication using dynamic programming.

# Summary

This practical implemented Chain Matrix Multiplication using Dynamic Programming. The algorithm finds the optimal order of multiplying a sequence of matrices to minimize the total number of scalar multiplications. Dynamic Programming stores the results of smaller matrix chains and uses them to solve larger chains. The practical also analyzed the execution time, time complexity, and space complexity.

# Conclusion

The Dynamic Programming approach efficiently determines the minimum multiplication cost for a chain of matrices. It avoids calculating the same subproblems repeatedly and provides an optimal multiplication order. The algorithm has O(n³) time complexity and O(n²) space complexity, making it much more efficient than checking every possible parenthesization directly.

# Practical 7 : Implementation of making a change problem using dynamic programming

# Summary : 

This practical implemented the Making Change Problem using Dynamic Programming. The algorithm finds the minimum number of coins required to make a given amount. Dynamic Programming stores previously calculated results to avoid repeated calculations. The practical also measured the execution time and analyzed the algorithm's time and space complexity.

# Conclusion : 

The Dynamic Programming approach efficiently solves the Making Change Problem by breaking it into smaller subproblems. It avoids unnecessary repeated calculations and provides the optimal minimum number of coins. The algorithm has O(amount × number of coins) time complexity and O(amount) space complexity.


# Practical 8 : Implementation of Graph and Searching (DFS and BFS).
# Summary : 
This practical implemented Graph Traversal using DFS and BFS in Python. DFS explores a graph by going as deep as possible before backtracking, while BFS explores vertices level by level using a queue. Both algorithms visit vertices and edges efficiently with O(V + E) time complexity. The practical helped in understanding graph representation and traversal techniques.

# Conclusion : 

The practical successfully demonstrated DFS and BFS graph traversal algorithms. DFS uses a stack/recursion approach, while BFS uses a queue. Both have O(V + E) time complexity, but their traversal order is different. These algorithms are fundamental techniques for solving various graph-related problems.
