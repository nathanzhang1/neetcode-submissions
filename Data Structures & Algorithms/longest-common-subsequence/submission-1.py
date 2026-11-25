class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        LCS = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    LCS[i][j] = 1 + LCS[i+1][j+1]
                else:
                    LCS[i][j] = max(LCS[i][j+1], LCS[i+1][j])
        
        return LCS[0][0]

'''
ace
abcde

DP table setup:

      i
    a c e
  a       0
  b       0
j c       0
  d       0
  e       0

Start at top left
If both chs same, look diagonally (i+1, j+1)
If both chs not same, look down and right and choose max((i+1, j), (i, j+1))

Base case: LCS[i][j] = 0 for i = len(text1) or j = len(text2)
Recurrence relation
    If text1[i] == text2[j], LCS[i][j] = 1 + LCS[i+1][j+1]
    If text1[i] != text2[j], LCS[i][j] = max(LCS[i+1][j], LCS[i][j+1])
Loop backwards for text1 and text2
'''