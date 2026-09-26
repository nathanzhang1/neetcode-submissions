class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_freqs = {x : 0 for x in range(26)}
        s2_freqs = {x : 0 for x in range(26)}

        for ch in s1:
            idx = ord(ch) - ord('a')
            s1_freqs[idx] += 1
                
        left, right = 0, len(s1) - 1

        p = left
        while p <= right:
            idx = ord(s2[p]) - ord('a')
            s2_freqs[idx] += 1
            p += 1
        
        matches = 0

        for ch in s2_freqs:
            if s1_freqs[ch] == s2_freqs[ch]:
                matches += 1
        
        if matches == 26:
            return True
                
        left += 1
        right += 1

        while right < len(s2):
            idx_left = ord(s2[left-1]) - ord('a')
            idx_right = ord(s2[right]) - ord('a')
            prev_left = s2_freqs[idx_left]
            prev_right = s2_freqs[idx_right]
            s2_freqs[idx_left] -= 1
            s2_freqs[idx_right] += 1

            if s1_freqs[idx_left] == prev_left and s1_freqs[idx_left] != s2_freqs[idx_left]:
                matches -= 1
            if s1_freqs[idx_left] != prev_left and s1_freqs[idx_left] == s2_freqs[idx_left]:
                matches += 1
            if s1_freqs[idx_right] == prev_right and s1_freqs[idx_right] != s2_freqs[idx_right]:
                matches -= 1
            if s1_freqs[idx_right] != prev_right and s1_freqs[idx_right] == s2_freqs[idx_right]:
                matches += 1
            
            if matches == 26:
                return True
            
            left += 1
            right += 1
        
        return False