class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0

        stack = []
        while i < n:
            ch = s[i]
            if ch != "]":
                stack.append(ch)
            else:
                curStr = ""
                while True:
                    curCh = stack.pop()
                    if curCh != "[":
                        curStr = curCh + curStr
                    else:
                        break

                repeats = ""
                while stack:
                    curCh = stack.pop()
                    if curCh in "1234567890":
                        repeats = curCh + repeats
                    else:
                        stack.append(curCh)
                        break

                for j in range(int(repeats)):
                    for k in curStr:
                        stack.append(k)
            i += 1
        
        return "".join(stack)

# Stack
# i points to position in s
# While i is not at end of s
    # If s[i] is not ], append to stack
    # If it is
        # Pop from stack curString until we have popped [
        # Pop from stack repeats until we see a non digit
        # Append curString to stack repeats times