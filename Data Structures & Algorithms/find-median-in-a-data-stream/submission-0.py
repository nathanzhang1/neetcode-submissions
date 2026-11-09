import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap, -num)
            return
        
        if num < -1 * self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            num = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, num)
        elif len(self.minheap) > len(self.maxheap) + 1:
            num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-1 * self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Keep 2 heaps that split data stream into half with smaller numbers and half with bigger numbers
# Top of maxheap of smaller numbers and top of minheap of bigger numbers is where median is
# Processing addNum:
    # First num: add to either max or minheap (we pick maxheap)
    # Num i: if num < top of maxheap add to maxheap, else add to minheap
        # If after adding length of max and minheap differ by >1, pop from longer heap and add to other heap
# Processing findMedian:
    # If both heaps have same length, median is top of both heaps / 2
    # If one heap is longer (by 1), median is top of that heap