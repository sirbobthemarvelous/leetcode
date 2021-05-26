class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        tallest = 0
        split = list(n)
        for x in split: 
            if int(x) > tallest: tallest = int(x)
                
        return tallest