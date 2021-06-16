class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #work backwards?
        #nvm it was always work backwards recursively
        step1 = 0
        step2 = 0
        for leg in range(len(cost)-1,-1,-1):
            #range works with start,stop,step
            step0 = cost[leg]+min(step1,step2)
            step2 = step1
            step1 = step0
        return min(step1,step2)
            
        
        
        