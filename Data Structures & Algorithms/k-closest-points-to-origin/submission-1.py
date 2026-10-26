import heapq
import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x * x + y * y)

            if len(heap) < k:
                heapq.heappush(heap, [-dist, x, y])
            else:
                furthest = -1 * heap[0][0]
                if dist < furthest:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-dist, x, y])
                else:
                    continue
        
        out = []
        while heap:
            _, x, y = heapq.heappop(heap)
            out.append([x, y])
        
        return out


# Max-heap capped at size k always keeps the k closest points
# We want all points up until K-th closest = K-th lowest Euclidean distance
# Iterate through points
    # Calculate its Euclidean distance
    # If adding new point would not exceed length of heap (k)
        # Heappush the new point
    # Elif adding new point would exceed length of heap (k) and new point is closer to furthest point (top)
        # Heappop the furthest point
        # Heappush the new point
    # Else (already at length k, new point is further)
        # This point is not useful, skip
# Go through the rest of the heap and return the points

# Minheap solution:

        # heap = []
        # for p in points:
        #     x, y = p[0], p[1]
        #     dist = sqrt(x * x + y * y)
        #     heap.append((dist, x, y))

        # heapq.heapify(heap)
        
        # out_list = []
        # for _ in range(k):
        #     _, x, y = heapq.heappop(heap)
        #     out_list.append([x, y])
        
        # return out_list