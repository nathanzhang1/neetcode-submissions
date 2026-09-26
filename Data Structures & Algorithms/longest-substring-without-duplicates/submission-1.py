class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = set()
        max_length = 0

        if len(s) == 0:
            return max_length
        
        seen.add(s[left])
        max_length += 1

        while True:
            if right == len(s) - 1:
                break
            
            right += 1
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length