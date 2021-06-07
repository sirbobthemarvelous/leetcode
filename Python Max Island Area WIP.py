class Solution(object):
    temp =0
    def checkDir(x,y):
        temp+=1
        grid[x][y] =2
            
        try:
            if grid[x][y+1] == 1:
                checkDir(x,y+1)
        except:
            pass
        try:
            if grid[x][y-1] == 1:
                checkDir(x,y-1)
        except:
            pass
        try:
            if grid[x+1][y] == 1:
                checkDir(x+1,y)
        except:
            pass
        try:
            if grid[x-1][y] == 1:
                checkDir(x-1,y)
        except:
            pass
        return void
        
    def maxAreaOfIsland(self, grid):
        maximum =0
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for ex in range(0, len(grid)):
            for why in range(0, len(grid[0])):
                if grid[ex][why] == 1:
                    checkDir(ex,why)
                    if temp > maximum:
                        maximum = temp
                    temp = 0
        
        return maximum
        