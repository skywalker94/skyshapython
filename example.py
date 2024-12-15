from skyshapython import MaxHeap, MinHeap

max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(20)
max_heap.push(5)

# Example 1: Using __len__
print(len(max_heap))  # Output: 3

# Example 2: Using __bool__
if max_heap:
    print("Heap is not empty")  # Output: Heap is not empty

# Removing all elements
max_heap.pop()
max_heap.pop()
max_heap.pop()

if not max_heap:
    print("Heap is empty")  # Output: Heap is empty

min_heap = MinHeap()

# Add some elements
min_heap.push(10)
min_heap.push(20)
min_heap.push(5)

# Pop the smallest item
print(min_heap.pop())  # Output: 5

# Push and pop in one operation
print(min_heap.pushpop(15))  # Output: 10

# Peek at the smallest item
print(min_heap.peek())  # Output: 15

# Example of len() and bool()
print(len(min_heap))  # Output: 2
if min_heap:
    print("Heap is not empty")  # Output: Heap is not empty

# Clear the heap
min_heap.pop()
min_heap.pop()

if not min_heap:
    print("Heap is empty")  # Output: Heap is empty