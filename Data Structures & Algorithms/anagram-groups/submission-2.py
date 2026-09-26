class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]
        
        out = []
        for anagram in anagram_map:
            out.append(anagram_map[anagram])
        
        return out

# Have a map: sorted -> list of all strings that when sorted = sorted string     
# For each string
    # If the sorted string is in map, add original string to list
    # Else add as new addition to map
# Iterate through map and add all the values to out list