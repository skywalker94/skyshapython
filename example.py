from skyshapython import MaxHeap, MinHeap

vals = [1, 77, 82, 15, 22, 43, 9, 8, 321, -3, 0]
print(f"Raw Values: {vals}")
max_heap = MaxHeap()
min_heap = MinHeap()

max_heap.push(vals)
min_heap.push(vals)

print(f"Ascending values: {min_heap.pop(50)}")
print(f"Descending values: {max_heap.pop(50)}")

#One step approach
print(f"Ascending values:{min_heap.pushpop(vals)}")
print(f"Descending values:{max_heap.pushpop(vals)}")