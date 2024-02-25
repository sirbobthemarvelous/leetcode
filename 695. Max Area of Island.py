class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited cells
        visit = set()

        # Depth-First Search (DFS) function to explore the island from a given cell
        def dfs(r, c):
            # Base cases:
            # If the cell is out of bounds or water (0) or already visited, return 0
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            # Mark the current cell as visited
            visit.add((r, c))
            # Explore adjacent cells in all four directions and count the area
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        # Initialize the maximum area of the island
        area = 0
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell represents land (1) and hasn't been visited yet
                if grid[r][c] == 1 and (r, c) not in visit:
                    # Calculate the area of the island starting from this cell
                    area = max(area, dfs(r, c))
        # Return the maximum area of the island
        return area
        """
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
        #"""
        """
        :type grid: List[List[int]]
        :rtype: int
        #"""
        for ex in range(0, len(grid)):
            for why in range(0, len(grid[0])):
                if grid[ex][why] == 1:
                    checkDir(ex,why)
                    if temp > maximum:
                        maximum = temp
                    temp = 0
        
        return maximum
        """