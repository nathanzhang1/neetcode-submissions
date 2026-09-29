class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        comb_list = list(zip(position, speed))
        sorted_list = list(reversed(sorted(comb_list, key=lambda x: x[0])))

        res_stack = []

        for p, s in sorted_list:
            time_to_target = (target - p) / s
            if res_stack and time_to_target <= res_stack[-1]:
                continue
            res_stack.append(time_to_target)
        
        return len(res_stack)

# Time needed for car i to reach target = (target - position[i]) / speed[i]
# Sort by (position, time)
# Iterate through list
    # If new car's time to target <= top of stack, don't push it to stack
    # Otherwise push it to stack
# Number of fleets = number of cars in stack


# [10, 8, 0, 5, 3]
# [10, 8, 5, 3, 0]
# [1, 1, 7, 3, 12]