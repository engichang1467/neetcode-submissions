import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num > self.max_heap[0]:
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -1 * num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1 * val)

    def findMedian(self) -> float:
        
        if len(self.min_heap) > len(self.max_heap):
            return -1 * self.min_heap[0]
        if len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]
        
        median_even = (-1 * self.min_heap[0] + self.max_heap[0]) / 2
        return median_even
        
        