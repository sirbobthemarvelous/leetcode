class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {} #hash map

        for i,n in enumerate(s):
            if n not in dict:
                dict[n] = i
            else:
                dict[n] = -1

        smallest = 100001
        #remove the duplicates with comprehension?

        dictComp = {key: value for key, value in dict.items() if value != -1}
        if len(dictComp) == 0:
            return -1

        for index in dictComp.values():
            if index < smallest:
                smallest = index
        return smallest