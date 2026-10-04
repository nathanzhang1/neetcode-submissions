import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        def eatable(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h

        while left <= right:
            k = (left + right) // 2
            if eatable(k):
                res = k
                right = k-1
            else:
                left = k+1
        
        return res


# Do binary search from 1 to max(piles) for minimum k
# At a given k
    # If eatable then right = k-1
    # If not eatable then left = k+1
# Piles are eatable at k if we go through each pile and sum of ceil(pile[i] / k) <= h