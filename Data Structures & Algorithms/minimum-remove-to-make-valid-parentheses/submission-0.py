class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        output = ''
        stack = []
        open_count = 0
        close_count = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            elif ch == ')':
                close_count += 1
            
            if close_count > open_count:
                close_count -= 1
                continue
            else:
                stack.append(ch)
        
        open_count, close_count = 0, 0
        
        for _ in range(len(stack)):
            ch = stack.pop()
            if ch == '(':
                open_count += 1
            elif ch == ')':
                close_count += 1
            
            if close_count < open_count:
                open_count -= 1
                continue
            else:
                output = ch + output

        return output