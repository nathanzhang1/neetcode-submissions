class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        left, right = 0, 1
        char_set = set()
        char_set.add(s[left])
        max_length = 0
        while right != len(s):
            if s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            else:
                char_set.add(s[right])
                if len(char_set) > max_length:
                    max_length = len(char_set)
                right += 1
        
        return max_length

# Sliding window: left = 0, right = 1, increment right and keep adding new char to set, increment left 
# when dup char found and keep doing this until that dup char is removed from set

# abcadbcbb
# pwwkew
# abcdeffghijkl
# abcdefaghijkl