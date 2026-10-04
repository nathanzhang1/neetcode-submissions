class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left, right = 0, 0

        if len(s) == 0:
            return 0
        
        char_set.add(s[right])
        maxLength = 1

        while right < (len(s) - 1):
            right += 1
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength


# Sliding window solution:

# Left and right at start
# While right is not at the end
    # Advance right
    # While right is in set
        # Remove left from set
        # Advance left
    # Add right to set
    # Update maxLength by right - left if possible