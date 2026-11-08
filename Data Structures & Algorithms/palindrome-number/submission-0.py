class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            if x // div != x % 10:
                return False
            
            x = (x % div) // 10
            div = div // 100
        
        return True


        # num = str(x)

        # if num[0] == "-":
        #     return False
        
        # return num == num[::-1]

# Nontrivial solution (two pointers)
# At each iteration extract the first and last digits and compare them until we get no digits or 1 left
# First digit = x // div where div = len(x) ie. len(x) = 5 -> div = 10000
# Last digit = x % 10
# Remove first and last digit: x = (x % len(x)) // 10
# Update length: length -= 2