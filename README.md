# skyshapython

**A Python library for utilities and wrappers for frequently used functionality.**

skyshapython is a lightweight and intuitive Python library designed to simplify common programming tasks. It currently includes easy-to-use wrappers for working with MaxHeap and MinHeap, extending Python's built-in functionality in a clean and efficient way. The library is licensed under the MIT license, ensuring it is free for anyone to use, modify, and distribute.

---

## Installation

You can install skyshapython directly from PyPI:

```bash
pip install skyshapython
```

---

## Links

- **PyPI**: [skyshapython on PyPI](https://pypi.org/project/skyshapython/)
- **GitHub**: [skyshapython Repository](https://github.com/skywalker94/skyshapython)
- **Website**: [Author Website](https://cv.sharangdeo.online/)

---

## Features

### **MaxHeap**
A simple wrapper for Python's `heapq` module, providing an easy-to-use MaxHeap implementation.

> Supports pushing single values or lists, and popping single or multiple values.

**Usage:**

```python
from skyshapython import MaxHeap

# Initialize the MaxHeap as default, with a value, or list
max_heap = MaxHeap() # default
max_heap_value = MaxHeap(5) # with a value
max_heap_list = MaxHeap([5, 2, 7, 4, 1, 9]) # with a list

# Add items to the heap
max_heap.push(10)
max_heap.push(20)
max_heap.push(5)

# Add multiple items at once
max_heap.push([50, 30, 40])

# Get the largest item
largest = max_heap.pop()
print(largest)  # Output: 50 (the largest value)

# Peek at the largest item without removing it
print(max_heap.peek())  # Output: 40 (the next largest)

# Add and pop in one operation (adding a single item)
max_heap.pushpop(15)  # Adds 15 and removes the largest element

# Add and pop multiple items in one operation
max_heap.pushpop([100, 200])  # Adds [100, 200], pops and returns the 2 largest values

# It can pop multiple items at once
max_heap.pop(2) # Outputs 2 largest values in order

# pop all remaining values in descending order
max_heap.popall()

# Check if the heap is empty
if max_heap:
    print("Heap is not empty")

# check length of the heap, number of values in it
print(len(max_heap))
```

---

### **MinHeap**
A clean wrapper for Python's `heapq` module, providing an intuitive MinHeap implementation.

> Supports pushing single values or lists, and popping single or multiple values.

**Usage:**

```python
from skyshapython import MinHeap

# Initialize the MinHeap as default, with a value, or list
min_heap = MinHeap() # default
min_heap_value = MinHeap(5) # with a value
min_heap_list = MinHeap([5, 2, 7, 4, 1, 9]) # with a list

# Add items to the heap
min_heap.push(10)
min_heap.push(20)
min_heap.push(5)

# Add multiple items at once
min_heap.push([50, 30, 40])

# Get the smallest item
smallest = min_heap.pop()
print(smallest)  # Output: 5 (the smallest value)

# Peek at the smallest item without removing it
print(min_heap.peek())  # Output: 10 (the next smallest)

# Add and pop in one operation (adding a single item)
min_heap.pushpop(15)  # Adds 15 and removes the smallest element

# Add and pop multiple items in one operation
min_heap.pushpop([100, 200])  # Adds [100, 200], pops and returns the 2 smallest values

# It can pop multiple items at once
min_heap.pop(2)  # Outputs 2 smallest values in order

# pop all remaining values in ascending order
min_heap.popall()

# Check if the heap is empty
if not min_heap:
    print("Heap is empty")

# Check length of the heap, number of values in it
print(len(min_heap))
```

---

### **SortMaster**
A versatile class that provides a variety of sorting algorithms, including basic sorting techniques as well as multi-threaded and optimized approaches.

> Supports sorting using algorithms like QuickSort, MergeSort, Timsort, IntroSort, and even a custom multi-threaded sorting implementation.

Sorting Methods:
- Bubble Sort: A simple comparison-based sorting algorithm.
- Selection Sort: A comparison-based sorting method that repeatedly selects the smallest element.
- Quick Sort: A divide-and-conquer sorting algorithm, often the fastest for large datasets.
- Merge Sort: A stable, comparison-based sorting algorithm using the divide-and-conquer approach.
- Insertion Sort: A comparison-based sorting method that builds the sorted list one element at a time.
- Heap Sort: A comparison-based sorting algorithm based on binary heaps.
- Timsort:  A hybrid sorting algorithm derived from MergeSort and InsertionSort, used in Python's built-in sorting.
- Intro Soft: A hybrid sorting algorithm combining QuickSort, HeapSort, and InsertionSort.
- Thread Sort: A multi-threaded sorting algorithm that uses multiple threads to speed up sorting on large datasets. (custom sorting solution)

Amusing Methods:
- Sleep Sort: A quirky and inefficient sorting algorithm that "sleeps" for a duration proportional to each number’s value and outputs them in order of completion.
- Bogosort: A highly inefficient and random sorting algorithm that repeatedly shuffles the list until it happens to be sorted.

> I cannot recommend the 'amusing' sorting methods. They can work, but they are very inefficient. The inspiration behind them was simply 'because I can'.

**Usage:**

```python
from skyshapython import SortMaster

# Initialize the SortMaster instance
sort_master = SortMaster()

# Sorting with BubbleSort (ascending and descending order)
arr = [5, 2, 9, 1, 5, 6]
sorted_asc = sort_master.bubble_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.bubble_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with SelectionSort (ascending and descending order)
sorted_asc = sort_master.selection_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.selection_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with QuickSort
sorted_asc = sort_master.quick_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.quick_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with MergeSort
sorted_asc = sort_master.merge_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.merge_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with InsertionSort
sorted_asc = sort_master.insertion_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.insertion_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with HeapSort
sorted_asc = sort_master.heap_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.heap_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with Timsort
sorted_asc = sort_master.timsort(arr.copy(), reverse=False)
sorted_desc = sort_master.timsort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with IntroSort
sorted_asc = sort_master.introsort(arr.copy(), reverse=False)
sorted_desc = sort_master.introsort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting with ThreadSort (multi-threaded sorting)
sorted_asc = sort_master.thread_sort(arr.copy(), reverse=False)
sorted_desc = sort_master.thread_sort(arr.copy(), reverse=True)

print(sorted_asc)  # Output: [1, 2, 5, 5, 6, 9]
print(sorted_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Finding the fastest sorting algorithm
fastest_algo = sort_master.fastest(arr.copy(), reverse=False)
print(fastest_algo)  # Output: 'QuickSort', 'MergeSort', 'Timsort', or 'IntroSort'
```

---

## License

skyshapython is licensed under the **MIT License**, which means you are free to use, modify, and distribute the library in both personal and commercial projects. Contributions are always welcome, so feel free to fork the repository and create pull requests for improvements or new features.

```text
MIT License

Copyright (c) 2024 skywalker94

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests on the [GitHub repository](https://github.com/skywalker94/skyshapython).

**Note** - As long as the library is in version `0.x.x` I am not actively looking after this. When I do intend to start managing and supporting this more seriously, I will upgrade to versions `1.0` and above. Thank you.

---

## Author

**skywalker94**
- [GitHub Profile](https://github.com/skywalker94)
- [Website](https://cv.sharangdeo.online)

**Note** - To be fair I do not know how often I will check back with this library and look through suggested pull requests as so on.. At the time of writing this up I just wanted to make heaps easier for myself (I detest the heapq syntax. It feels like such a chore & I often forget it). In the future, I may add mode functionality to this and change my approach toward this tiny library. But until then.. godspeed!

---

Happy coding with **skyshapython**! 🎉