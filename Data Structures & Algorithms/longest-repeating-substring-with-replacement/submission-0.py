class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        char_freqs = {}
        max_freq, max_len = 0, 0

        while right < len(s):

            if s[right] not in char_freqs:
                char_freqs[s[right]] = 0
            char_freqs[s[right]] += 1

            max_freq = max(max_freq, char_freqs[s[right]])

            if right - left + 1 - max_freq > k:
                char_freqs[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)

            right += 1

        
        return max_len