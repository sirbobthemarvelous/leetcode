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
        