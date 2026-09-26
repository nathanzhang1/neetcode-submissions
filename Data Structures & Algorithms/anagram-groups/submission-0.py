class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_list = []
        for string in strs:
            if len(out_list) == 0:
                out_list.append([string])
            else:
                counter = 0
                for group in out_list:
                    if self.isAnagram(string, group[0]):
                        group.append(string)
                        break
                    counter += 1
                if counter == len(out_list):
                    out_list.append([string])
        return out_list
    
    def isAnagram(self, str1, str2):
        hashmap = {}
        for char in str1:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in str2:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
            if hashmap[char] == 0:
                hashmap.pop(char)
        if len(hashmap) == 0:
            return True
        return False