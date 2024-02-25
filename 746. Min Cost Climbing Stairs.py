class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])

"""class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step = len(cost)
        if (step > 1):
            return min(self.minCostClimbingStairs(cost[:step-1]),self.minCostClimbingStairs(cost[:step-2])) 
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
            
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #work backwards?
        #work forwards just check the next FOUR step costs
        minimum = 0
        if len(cost) == 2:
            if cost[1]<cost[0]:
                return cost[1]
            return cost[0]
        if len(cost) == 3:
            if cost[0]+cost[2] < cost[1]:
                return cost[0]+cost[2]
            return cost[1]
        if len(cost)==4:
            return min(cost[0]+cost[2],cost[1]+cost[2],cost[1]+cost[3])
        
        leg=-1
        while leg<len(cost):
            if leg == len(cost)-4:
                if cost[leg+1]+cost[leg+3] < cost[leg+2]:
                    return minimum+cost[leg+1]+cost[leg+3]
                return minimum+cost[leg+2]
            if leg == len(cost)-3:
                return minimum+cost[min(cost[leg+1],cost[leg+2])]
            #if leg == len(cost)-2:
                #return minimum
            steady = cost[leg+1]+cost[leg+3]
            hop = cost[leg+2]+cost[leg+3]
            quick = cost[leg+2]+cost[leg+4]
            if min(steady,hop,quick) == steady:
                leg+=1
                minimum+=cost[leg]
            else:
                leg+=2
                minimum+=cost[leg]
            
            
        return minimum
        """
        
        