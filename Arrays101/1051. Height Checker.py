class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) < 2: return 0
        list2 = sorted(heights)
        lcomp = [i for i in range(len(heights)) if heights[i] != list2[i]]
        """
        result = 0
        for (x,y) in zip(heights, list2):
            if(x!=y): result+=1
        """
        return len(lcomp)
        