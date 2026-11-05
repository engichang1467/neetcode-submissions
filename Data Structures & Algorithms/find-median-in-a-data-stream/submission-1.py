import heapq

class MedianFinder:

    def __init__(self):
        self.curr_list = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.curr_list, num)
        new_list = []
        while self.curr_list:
            new_list.append(heapq.heappop(self.curr_list))
        self.curr_list = new_list

    def findMedian(self) -> float:
        n = len(self.curr_list) 
        mid = n // 2
        if n % 2 == 0:
            median_even = (self.curr_list[mid-1] + self.curr_list[mid]) / 2
            return median_even
        return self.curr_list[mid]
        
        