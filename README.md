# Assignment3
This repository contains my work for a project that involves analyzing and implementing two key algorithms: Randomized Quicksort and Hashing with Chaining. The project is divided into two main parts, each focusing on a different algorithm, with detailed implementation and performance testing.

Project Overview

In Part 1, I implemented and analyzed Randomized Quicksort, a widely-used sorting algorithm that introduces randomness into the pivot selection process to improve performance in various cases, such as when the array is already sorted or reverse-sorted. The goal was to explore how this randomized approach affects the algorithm's time complexity and performance compared to Deterministic Quicksort.

In Part 2, I implemented a Hash Table with Chaining, a data structure that allows efficient key-value storage and collision resolution using linked lists. This part of the project focused on understanding how hashing works, how collisions are handled, and how different operations (insert, search, delete) perform under different conditions.

File Structure
/part1_randomized_quick_sort.py       # Implementation of Randomized Quicksort and comparison with Deterministic Quicksort
/part2_hashing_with_chaining.py        # Implementation of Hash Table with Chaining (insert, search, delete)
/README.md                            # Project overview and instructions (this file)

Part 1: Randomized Quicksort
Overview:

In this part of the project, I implemented Randomized Quicksort, which is known for its efficiency in most cases due to the random selection of pivots. I also compared its performance against Deterministic Quicksort, which always uses the first element as the pivot.

How It Works:

Randomized Quicksort: A random element is selected as the pivot to partition the array into smaller subarrays. The algorithm then recursively sorts these subarrays.

Deterministic Quicksort: The first element of the array is always chosen as the pivot, which can result in unbalanced partitions, especially when the array is already sorted or nearly sorted.

Time Complexity:

Average Case: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)

Worst Case: 
𝑂
(
𝑛
2
)
O(n
2
), though highly unlikely with randomized pivots.

Empirical Comparison:

I tested both sorting algorithms on:

Randomly generated arrays

Already sorted arrays

Reverse-sorted arrays

Arrays with repeated elements

The results showed that Randomized Quicksort performed significantly better on sorted and reverse-sorted arrays compared to Deterministic Quicksort.

How to Run:

To run the Randomized Quicksort and see the performance comparison, simply execute the Python script part1_randomized_quick_sort.py.

python part1_randomized_quick_sort.py

Part 2: Hashing with Chaining
Overview:

In Part 2, I implemented a Hash Table with Chaining, which resolves hash collisions by storing multiple key-value pairs at the same index in a linked list.

How It Works:

Hash Table: The hash table uses a simple hash function to calculate an index for each key. If multiple keys hash to the same index, they are stored in a linked list at that index.

Operations:

Insert: Adds a new key-value pair to the hash table.

Search: Retrieves the value associated with a given key.

Delete: Removes a key-value pair from the hash table.

Time Complexity:

Average Case:

Insert, Search, Delete: 
𝑂
(
1
)
O(1) (assuming a good hash function with minimal collisions).

Worst Case:

Insert, Search, Delete: 
𝑂
(
𝑛
)
O(n) if all keys hash to the same index.

How to Run:

To test the hash table and its operations, run the script part2_hashing_with_chaining.py.

python part2_hashing_with_chaining.py

Example Operations:

The hash table supports the following operations:

Inserting key-value pairs.

Searching for values based on keys.

Deleting key-value pairs.

The example usage in the script demonstrates how to use these operations and shows the expected outputs for insertion, search, and deletion.

Testing and Results
Part 1: Randomized Quicksort

I ran performance tests for Randomized Quicksort and Deterministic Quicksort on various datasets. The tests showed that Randomized Quicksort significantly outperforms Deterministic Quicksort when the array is already sorted or reverse-sorted.

Part 2: Hashing with Chaining

The hash table with chaining was able to handle insertions, searches, and deletions efficiently, though performance degraded in cases with high collision rates. Testing on various types of data showed that the hash table is an effective data structure for managing key-value pairs, with performance closely tied to the hash function’s effectiveness in distributing keys.

Conclusion

This project provided me with a deeper understanding of Randomized Quicksort and Hashing with Chaining, two essential algorithms in computer science. By implementing these algorithms, I gained practical experience in algorithm design, implementation, and performance analysis. The tests and analysis confirmed the importance of choosing the right algorithm and data structure for a given problem, particularly in terms of time complexity and handling edge cases.

Future Improvements

Part 1: I could further optimize Randomized Quicksort by implementing a three-way partitioning scheme to handle arrays with many repeated elements more efficiently.

Part 2: I plan to enhance the hash table by implementing dynamic resizing to handle cases where the load factor grows too high, ensuring that the table remains efficient as more elements are inserted.
