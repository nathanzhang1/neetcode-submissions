class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""

        for char in s:
            if char.isalnum():
                alnum_s += char

        upper_s = alnum_s.upper()
        left, right = 0, len(upper_s) - 1

        while left < right:
            if upper_s[left] != upper_s[right]:
                return False
            left += 1
            right -= 1
        return True