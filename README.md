# Data Structures and Algorithms
Algorithms and data structures are fundamental to efficient code and good software design. Creating and designing excellent algorithms is required for being an exemplary programmer. This repository presents the Python code implementation of the provided algorithms and data structures from William Fiset at: https://github.com/williamfiset/Algorithms.

## Running an algorithm implementation

To run any of the algorithms here, you need at least Python version 3.9:

```
python <algorithm-filepath>
```

## Data Structures
- [Binary Search Tree](src/main/data_structures/binary_search_tree/binary_search_tree.py)
- [Fenwick Tree](src/main/data_structures/fenwick_tree/fenwick_tree.py)
- [Linked List](src/main/data_structures/linked_list/doubly_linked_list.py)
- [Priority Queue](src/main/data_structures/priority_queue/)
  - [Min Binary Heap](src/main/data_structures/priority_queue/binary_heap.py)
- [Queue](src/main/data_structures/queue)
  - [Queue (list)](src/main/data_structures/queue/array_queue.py)
  - [Queue (linked list)](src/main/data_structures/queue/linked_queue.py)
- [Stack](src/main/data_structures/stack/)
  - [Stack (list)](src/main/data_structures/stack/array_stack.py)
  - [Stack (linked list)](src/main/data_structures/stack/linked_stack.py)
- [Union Find](src/main/data_structures/union_find/union_find.py)

## Graph Theory
### Tree algorithms
- [Rooting an undirected tree](src/main/algorithms/graph/trees/rooting_tree.py) - O(V + E)
- [Identifying isomorphic trees](src/main/algorithms/graph/trees/tree_isomorphism.py) - O(?)

### Main graph theory algorithms
- [Breadth first search (adjacency list)](src/main/algorithms/graph/breadth_first_search_iterative.py) - O(V + E)
- [Depth first search (adjacency list, iterative)](src/main/algorithms/graph/depth_first_search_iterative.py) - O(V + E)
- [Depth first search (adjacency list, recursive)](src/main/algorithms/graph/depth_first_search_recursive.py) - O(V + E)

## Mathematics
- [Extended euclidean algorithm](src/main/algorithms/math/extended_euclidean_algorithm.py) - ~O(log(a + b))
- [Greatest Common Divisor (GCD)](src/main/algorithms/math/gcd.py) - ~O(log(a + b))
- [Primality check](src/main/algorithms/math/is_prime.py) - O(√n)
- [Least Common Multiple (LCM)](src/main/algorithms/math/lcm.py) - ~O(log(a + b))
- [Modular inverse](src/main/algorithms/math/modular_inverse.py) - ~O(log(a + b))

## Search algorithms
- [Binary search](src/main/algorithms/search/binary_search.py) - O(log(n))

## Sorting algorithms
- [Bubble sort](src/main/algorithms/sorting/bubble_sort.py) - O(n<sup>2</sup>)
- [Bucket sort](src/main/algorithms/sorting/bucket_sort.py) - Θ(n + k)
- [Counting sort](src/main/algorithms/sorting/counting_sort.py) - O(n + k)
- [Heapsort](src/main/algorithms/sorting/heapsort.py) - O(nlog(n))
- [Insertion sort](src/main/algorithms/sorting/insertion_sort.py) - O(n<sup>2</sup>)
- [Mergesort](src/main/algorithms/sorting/merge_sort.py) - O(nlog(n))
- [Quicksort](src/main/algorithms/sorting/quick_sort.py) - Θ(nlog(n))
- [Selection sort](src/main/algorithms/sorting/selection_sort.py) - O(n<sup>2</sup>)

## String algorithms

## License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT).
In short, this means you are free to use this software in any personal, open-source or commercial projects. Attribution is optional but appreciated.
