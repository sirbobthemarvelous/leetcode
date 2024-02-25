class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
        """
        first = strs[0]
        shared = ''
        index = 0
        for word in strs:
            
            if index > len(word): break


            """