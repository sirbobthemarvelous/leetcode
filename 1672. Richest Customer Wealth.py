class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxVal = 0
        for x in range(len(accounts)):
            running = 0
            for y in range(len(accounts[0])):
                running += accounts[x][y]
            if running > maxVal: maxVal = running
        return maxVal

"""
leetcode reminded me of the defined functions
def maximumWealth(self, accounts: List[List[int]]) -> int:
	maxWealth = 0
	for i in range(len(accounts)):
		totalWealth = sum(accounts[i])
		maxWealth = max(maxWealth, totalWealth)
	return maxWealth
I tried it out, it's slower but it still works
""" 
        