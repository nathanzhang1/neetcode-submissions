class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        curLongest = strs[0]

        for s in strs:
            while not s.startswith(curLongest):
                if curLongest == "":
                    return ""
                curLongest = curLongest[:-1]
        
        return curLongest

# Take first str as curLongest
# For the rest of strs, on str i
    # While str.startswith(curLongest) is false
        # If curLongest is empty, return ""
        # Shorten curLongest by 1 ch at the end: curLongest = curLongest[:-1]
