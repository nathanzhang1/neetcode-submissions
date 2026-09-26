class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output = []

        for s in strs:
            ch_count = [0] * 26
            for ch in s:
                ch_count[ord(ch) - ord("a")] += 1
            tup_count = tuple(ch_count)
            if tup_count not in anagrams:
                anagrams[tup_count] = []
            anagrams[tup_count].append(s)
        
        for an in anagrams:
            output.append(anagrams[an])
        
        return output