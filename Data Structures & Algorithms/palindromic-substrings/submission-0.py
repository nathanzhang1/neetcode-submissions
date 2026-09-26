class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        out = 0

        for i in range(N):
            left, right = i, i
            while left >= 0 and right < N and s[left] == s[right]:
                out += 1
                left -= 1
                right += 1
        
        for i in range(N-1):
            left, right = i, i+1
            while left >= 0 and right < N and s[left] == s[right]:
                out += 1
                left -= 1
                right += 1
        
        return out