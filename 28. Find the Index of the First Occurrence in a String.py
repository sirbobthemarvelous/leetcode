class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLength = len(needle)
        if(len(haystack) == nLength):
            if(haystack == needle): return 0
            return -1
        for x in range(1+len(haystack)-nLength):
            if(haystack[x:x+nLength]==needle): return x
        return -1
        