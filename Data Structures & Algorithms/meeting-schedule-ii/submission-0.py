"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: (x.start, x.end))

        if len(intervals) == 0:
            return 0
        
        days = 1
        heap = []

        for i in intervals:
            if not heap:
                heapq.heappush(heap, i.end)
                continue

            if i.start < heap[0]:
                days += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        
        return days
        
        # Sort intervals by their start time
        # For each interval
            # If start time < top of minheap
                # Insert end time into minheap
                # Days++
            # Else start time >= top of minheap
                # Pop from minheap
                # Insert end time into minheap