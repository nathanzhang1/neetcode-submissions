class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen = 0, 0

        for ch in s:
            if ch == "(":
                minOpen += 1
                maxOpen += 1
            elif ch == ")":
                minOpen -= 1
                maxOpen -= 1
                if minOpen < 0:
                    minOpen = 0
                if maxOpen < 0:
                    return False
            elif ch == "*":
                minOpen -= 1
                maxOpen += 1
                if minOpen < 0:
                    minOpen = 0
        
        return minOpen == 0