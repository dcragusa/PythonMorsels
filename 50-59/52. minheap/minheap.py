import heapq


class MinHeap:
    def __init__(self, iterable, key=lambda x: x):
        self.key = key
        self.heap = [(key(i), i) for i in iterable]
        heapq.heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, (self.key(item), item))

    def peek(self):
        return self.heap[0][1]

    def pop(self):
        item = heapq.heappop(self.heap)
        return item[1]


class MaxHeap:
    def __init__(self, iterable, key=lambda x: x):
        self.key = key
        self.heap = [(key(i), i) for i in iterable]
        heapq._heapify_max(self.heap)

    def __len__(self):
        return len(self.heap)

    def push(self, item):
        self.heap.append((self.key(item), item))
        heapq._siftdown_max(self.heap, 0, len(self.heap)-1)

    def peek(self):
        return self.heap[0][1]

    def pop(self):
        item = heapq._heappop_max(self.heap)
        return item[1]
