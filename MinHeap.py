class MinHeap:
    def __init__(self, data=None):
        self.heap = data or []
        if self.heap:
            self.build_min_heap()

    def parent(self, i): return (i - 1) >> 1
    def left(self, i): return (i << 1) + 1
    def right(self, i): return (i << 1) + 2

    def heapify(self, i):
        smallest, left, right = i, self.left(i), self.right(i)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]: smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def build_min_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)
    
    def push(self, item):
        self.heap.append(item)
        idx = len(self.heap) - 1
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            p = self.parent(idx)
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            idx = p
    
    def pop(self):
        if not self.heap: return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop() if len(self.heap) > 1 else None
        if self.heap[0] is not None: self.heapify(0)
        return root
    
    def __str__(self): return str(self.heap)

# Example usage
def example_usage():
    heap = MinHeap([10, 3, 5, 1, 4, 8])
    print("Heap after build:", heap)
    heap.push(2)
    print("Heap after push:", heap)
    print("Popped element:", heap.pop())
    print("Heap after pop:", heap)
example_usage()
