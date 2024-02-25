class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(1,len(dp[0])):
            dp[0][i]=sys.maxsize
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if(j>=coins[i-1]):
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        if(dp[len(coins)][amount]==sys.maxsize):
            return -1
        return dp[len(coins)][amount]