class Solution:
    def romanToInt(self, s: str) -> int:
        curSum = 0
        p = 0
        romToInt = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4
        }

        while p < len(s):
            rom = s[p]
            if rom == "C" and p+1 < len(s) and s[p+1] in "DM":
                p += 1
                rom += s[p]
            elif rom == "X" and p+1 < len(s) and s[p+1] in "LC":
                p += 1
                rom += s[p]
            elif rom == "I" and p+1 < len(s) and s[p+1] in "VX":
                p += 1
                rom += s[p]

            curSum += romToInt[rom]
            p += 1
        
        return curSum

# Process char by char
    # If M add 1000
    # If D add 500
    # If C add 100
        # If next is M add 800 more
        # If next is D add 300 more
    # If L add 50
    # If X add 10
        # If next is C add 80 more
        # If next is L add 30 more
    # If V add 5
    # If I add 1
        # If next is X add 8 more
        # If next is V add 3 more