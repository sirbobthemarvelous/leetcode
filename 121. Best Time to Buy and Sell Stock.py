class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        """
        bottom = prices[0]
        topSearch = False
        profit = 0
        for x in prices:
            if topSearch:
                newProfit = x - bottom
                if newProfit > profit:
                    proft = newProfit

            elif(x <= bottom): 
                bottom = x
                
            else:
                topSearch = True
                profit = x-bottom
        return profit """