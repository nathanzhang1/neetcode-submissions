class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        p = 0
        s = "".join(s.split())

        while p < len(s):
            char = s[p]
            if char.isdigit():
                num = char
                p += 1
                while p < len(s) and s[p].isdigit():
                    num += s[p]
                    p += 1
                stack.append(int(num))
            elif char == "-" or char == "+":
                stack.append(char)
                p += 1
            elif char == "*" or char == "/":
                a = stack.pop()
                p += 1
                b = s[p]
                p += 1
                while p < len(s) and s[p].isdigit():
                    b += s[p]
                    p += 1
                res = a * int(b) if char == "*" else a // int(b)
                stack.append(res)
        
        p = 1
        curOut = stack[0]
        while p < len(stack):
            op = stack[p]
            p += 1
            curOut = curOut + stack[p] if op == "+" else curOut - stack[p]
            p += 1
        
        return curOut


# Stack:
# Do first pass over strings and deal with * and /
# For each string
    # If num or + or - append to stack
    # If * or /
        # Pop from stack: a
        # Get next in string: b
        # Process operation: a * b or a // b and append result to stack
# Do second pass over stack as list to deal with remaining + and - operations
# Get front of list (use pointer), this is starting val
# While pointer not at end of list
    # Move pointer: this is + or -
    # Move pointer: this is next val
    # Process operation: cur_val +/- val