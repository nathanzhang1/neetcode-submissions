class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        temp_stack = []
        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                temp_val, temp_idx = temp_stack.pop()
                output[temp_idx] = i - temp_idx
            temp_stack.append((temp, i))
        return output