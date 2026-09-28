import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                op1, op2 = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                if t == "+":
                    res = op1 + op2
                if t == "-":
                    res = op1 - op2
                if t == "*":
                    res = op1 * op2
                if t == "/":
                    if (op1 / op2) >= 0:
                        res = op1 // op2
                    else:
                        res = math.ceil(op1 / op2)
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]


# Use stack
# For each token
    # If token is number push onto stack
    # If token is operand
        # Pop top 2 off stack
        # Apply operand
        # Push result onto stack
# At the end return top of stack