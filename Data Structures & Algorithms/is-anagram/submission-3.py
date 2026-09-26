class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = [char for char in s]
        tList = [char for char in t]
        return sorted(sList) == sorted(tList)
