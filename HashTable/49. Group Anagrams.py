class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} #hash map

        for n in strs:
            if len(n) > 1: #sort so anagrams match
                res = ''.join(sorted(n))
            else:
                res = n
            if res not in dict:
                dict[res] = [n] #be sure to add as list
            else:
                dict[res].append(n)
        
        return dict.values()
        