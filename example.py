from skyshapython import MaxHeap, MinHeap, SortMaster

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

sm = SortMaster()
print(f"Bubble Sorted: {sm.bubble_sort([1,2,7,4,3])}")
print(f"Timsort Sorted: {sm.timsort([1,2,7,4,3])}")
print(f"Quick Sorted: {sm.quick_sort([1,2,7,4,3])}")
print(f"Thread Sorted: {sm.thread_sort([1,2,7,4,3])}")
print(f"Fastest Algorithm with threading: {sm.fastest([1,2,7,4,3], display=True)}")

print(f"Bubble Sorted: {sm.bubble_sort([1,2,7,4,3], reverse=True)}")
print(f"Timsort Sorted: {sm.timsort([1,2,7,4,3], reverse=True)}")
print(f"Quick Sorted: {sm.quick_sort([1,2,7,4,3], reverse=True)}")
print(f"Thread Sorted: {sm.thread_sort([1,2,7,4,3], reverse=True)}")

# One of 4 potential outputs: QuickSort, MergeSort, Timsort, IntroSort
print(f"Fastest Algorithm with threading: {sm.fastest(list(range(100000)))}")