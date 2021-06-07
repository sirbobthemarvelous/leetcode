import operator
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        maximum =0
        mod = 1e9+7
        engineers = dict(zip(speed, efficiency))
        sortedEngineers = sorted(engineers.items(),key=operator.itemgetter(1), reverse=True)
        #performance = [] multiply speed and engineers
        
            
        for members in range(1,k):
            speeds = []
            multipliers = []
            for index, (key, value) in enumerate(engineers.items()):
                if len(speeds) >= members:
                    if sum(speeds)*min(multipliers) > maximum:
                        maximum = sum(speeds)*min(multipliers)
                    break
                else:
                    speeds.append(key)
                    multipliers.append(value)
            
        return maximum%mod
        