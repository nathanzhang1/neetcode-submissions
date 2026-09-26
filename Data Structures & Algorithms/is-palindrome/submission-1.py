class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for char in s:
            if char.isalnum():
                new_s.append(char.lower())

        front_index = 0
        back_index = len(new_s) - 1

        for char in new_s:
            if new_s[front_index] != new_s[back_index]:
                return False
            front_index += 1
            back_index -= 1
        return True