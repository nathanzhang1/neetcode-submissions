class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def build(opens, closes, s):
            if opens == n and closes == n:
                output.append(s)
                return
            
            if opens < n:
                build(opens + 1, closes, s + "(")
            if opens > closes:
                build(opens, closes + 1, s + ")")
        
        build(1, 0, "(")

        return output