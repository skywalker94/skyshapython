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

## Features

### **MaxHeap**
A simple wrapper for Python's `heapq` module, providing an easy-to-use MaxHeap implementation.

**Usage:**

```python
from skyshapython import MaxHeap

# Initialize the MaxHeap
max_heap = MaxHeap()

# Add items to the heap
max_heap.push(10)
max_heap.push(20)
max_heap.push(5)

# Get the largest item
largest = max_heap.pop()
print(largest)  # Output: 20

# Peek at the largest item without removing it
print(max_heap.peek())  # Output: 10

# Add and pop in one operation
max_heap.pushpop(15)  # Adds 15 and removes the largest element
print(max_heap.pop())  # Output: 10

# Check if the heap is empty
if max_heap:
    print("Heap is not empty")
```

---

### **MinHeap**
A clean wrapper for Python's `heapq` module, providing an intuitive MinHeap implementation.

**Usage:**

```python
from skyshapython import MinHeap

# Initialize the MinHeap
min_heap = MinHeap()

# Add items to the heap
min_heap.push(10)
min_heap.push(20)
min_heap.push(5)

# Get the smallest item
smallest = min_heap.pop()
print(smallest)  # Output: 5

# Peek at the smallest item without removing it
print(min_heap.peek())  # Output: 10

# Add and pop in one operation
min_heap.pushpop(15)  # Adds 15 and removes the smallest element
print(min_heap.pop())  # Output: 15

# Check if the heap is empty
if not min_heap:
    print("Heap is empty")
```

---

## Links

- **PyPI**: [skyshapython on PyPI](https://pypi.org/project/skyshapython/)
- **GitHub**: [skyshapython Repository](https://github.com/skywalker94/skyshapython)

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

**Note** - As long as the library is in version `0.x.x` I am not actively looking after this. When I do intend to start managing and supporting this more seriously, I will upgrade to versions above `1.0`.

---

## Author

**skywalker94**
- [GitHub Profile](https://github.com/skywalker94)
- [Website](https://cv.sharangdeo.online)

**Note** - To be fair I do not know how often I will check back with this library and look through suggested pull requests as so on.. At the time of writing this up I just wanted to make heaps easier for myself (I detest the heapq syntax. It feels like such a chore & I often forget it). In the future, I may add mode functionality to this and change my approach toward this tiny library. But until then.. godspeed!

Happy coding with **skyshapython**! 🎉