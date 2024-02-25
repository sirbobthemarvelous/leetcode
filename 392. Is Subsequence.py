class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        index1 = 0
        index2 = 1
        target = s[0]
        for ele in t:
            if ele == target:
                index1 +=1
            if index1 == len(s): return True
            target = s[index1]
        
        return False
            
