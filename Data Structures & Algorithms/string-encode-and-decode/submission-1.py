class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out = ""
        for string in strs:
            out = out + str(len(string)) + "|" + string

        print(out)
        return out
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        out_list = []
        num_list = [str(num) for num in range(0, 10)]
        i = 0
        while i < len(s):
            if s[i] in num_list:
                len_str = ""
                len_str += s[i]
                if s[i+1] in num_list:
                    i += 1
                    len_str += s[i]
                    if s[i+1] in num_list:
                        i += 1
                        len_str += s[i]
                if s[i+1] == "|":
                    length = int(len_str)
                    i += 2
                    out_str = ""
                    for j in range(length):
                        out_str += s[i]
                        i += 1
                    out_list.append(out_str)
        return(out_list)     

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Before each string, add the length of the string and a delimiter then in the decoder traverse the array using a pointer