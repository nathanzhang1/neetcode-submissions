import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        negative_weights = [-x for x in stones]
        heapq.heapify(negative_weights)

        while len(negative_weights) > 1:
            y = -1 * heapq.heappop(negative_weights)
            x = -1 * heapq.heappop(negative_weights)

            if x == y:
                continue
            elif x != y:
                heapq.heappush(negative_weights, -1 * (y-x))
        
        return -1 * negative_weights[0] if negative_weights else 0

# Turn stones into maxheap
# While there is more than 1 stone
    # Heappop top 2 stones y and x
    # If x == y continue
    # If x != y heappush y-x
# Return top of heap