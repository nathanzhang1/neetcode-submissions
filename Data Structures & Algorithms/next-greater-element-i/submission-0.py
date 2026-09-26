class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ht = {num: -1 for num in nums2}
        output = []

        for n in nums2:
            while stack and n > stack[-1]:
                i = stack.pop()
                ht[i] = n
            stack.append(n)
        
        for n in nums1:
            output.append(ht[n])
        
        return output