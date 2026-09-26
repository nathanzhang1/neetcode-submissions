class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
        
        return dp[0]