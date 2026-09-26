class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        prev, cur = x, x // 2

        while cur * cur > x:
            prev = cur
            cur = cur // 2
        
        left, right = cur, prev

        while left + 1 != right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
        
        return left if left * left <= x and right * right > x else right