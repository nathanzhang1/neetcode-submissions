class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
            else:
                prefix.append(prefix[i-1] * num)
        
        postfix = []
        nums.reverse()
        for i, num in enumerate(nums):
            if i == 0:
                postfix.append(num)
            else:
                postfix.append(postfix[i-1] * num)
        postfix.reverse()

        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(postfix[i + 1])
            elif i == len(nums) - 1:
                answer.append(prefix[i - 1])
            else:
                answer.append(prefix[i - 1] * postfix[i + 1])
        return answer
            
