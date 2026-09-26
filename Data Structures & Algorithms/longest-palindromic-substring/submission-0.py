class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        max_length = 0

        if len(s) <= 1:
            return s
        
        cur = 0
        while cur < len(s):
            cur_length = 1
            left, right = cur-1, cur+1
            if cur_length > max_length:
                max_length = cur_length
                output = s[cur]

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cur_length += 2
                    if cur_length > max_length:
                        max_length = cur_length
                        output = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break

            cur += 1
        
        curL, curR = 0, 1
        while curR < len(s):
            if s[curL] == s[curR]:
                cur_length = 2

                if cur_length > max_length:
                    max_length = cur_length
                    output = s[curL:curR+1]

                left, right = curL-1, curR+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        cur_length += 2
                        if cur_length > max_length:
                            max_length = cur_length
                            output = s[left:right+1]
                        left -= 1
                        right += 1
                    else:
                        break

            curL += 1
            curR += 1

        return output