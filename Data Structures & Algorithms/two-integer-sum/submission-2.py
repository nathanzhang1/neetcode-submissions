class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list = []
        first_index = 0
        for first_num in nums:
            second_index = first_index + 1
            for second_num in nums[first_index+1:len(nums)]:
                if (first_num + second_num) == target:
                    result_list = [first_index, second_index]
                    return result_list
                second_index += 1
            first_index += 1

