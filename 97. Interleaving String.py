class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        fails = 0
        firstplace = 0
        secondplace= 0
        thirdplace=0
        def checkSimilarities(small,large,index):
            size=0
            for update in range(index+1, len(large)+1):
                if small[index:].startswith(large[index:update]):
                    size+=1
                else:
                    break
                    
            return size
        
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        while thirdplace<len(s3):
            if fails==2:
                return False
            firstChunk = checkSimilarities(s1,s3,firstplace) 
            if firstChunk==0:
                fails+=1
            else:
                firstplace+= firstChunk
                thirdplace+= firstChunk
                fails = 0
            secondChunk = checkSimilarities(s2,s3,secondplace)
            if secondChunk==0:
                fails+=1
            else:
                secondplace+= secondChunk
                thirdplace+= secondChunk
                fails = 0
        
        if firstplace == len(s1) and secondplace==len(s2) and thirdplace==len(s3):
            return True
                
        return False
"""