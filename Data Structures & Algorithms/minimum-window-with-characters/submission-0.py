class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        s_freq, t_freq = {}, {}

        for ch in t:
            if ch not in t_freq:
                t_freq[ch] = 0
            t_freq[ch] += 1
        
        for ch in t_freq:
            if ch not in s_freq:
                s_freq[ch] = 0
        
        conditions_needed, conditions_met = len(t_freq), 0
        left, right = 0, 0
        min_len = float('inf')
        out_boundaries = (0, 0)

        while right < len(s):
            if s[right] not in s_freq:
                right += 1
                continue
            
            s_freq[s[right]] += 1
            if s_freq[s[right]] == t_freq[s[right]]:
                conditions_met += 1
            
            while conditions_met == conditions_needed:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    out_boundaries = (left, right)
                
                if s[left] in s_freq:
                    s_freq[s[left]] -= 1
                    if s_freq[s[left]] < t_freq[s[left]]:
                        conditions_met -= 1
                
                left += 1
                
            right += 1
        
        if min_len == float('inf'):
            return ""
        
        left, right = out_boundaries

        return s[left:right+1]