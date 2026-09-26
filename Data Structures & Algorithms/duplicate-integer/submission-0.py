class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numList = {}
        for num in nums:
            if num not in numList:
                numList[num] = num
            else:
                return True
        return False