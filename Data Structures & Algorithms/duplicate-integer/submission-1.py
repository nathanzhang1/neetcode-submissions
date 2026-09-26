class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []
        for num in nums:
            if num in nums_list:
                return True
            nums_list.append(num)
        return False