class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        visited = set()
        def bfs(i,j):
            q= deque()
            visited.add((i,j))
            q.append((i,j))
            while q:
                r,c = q.popleft()
                adj= [[1,0],[0,1],[-1,0],[0,-1]]
                for x, y in adj:
                    if (r+x) in range(m) and (c+y) in range(n) and grid[r+x][c+y] =='1' and (r+x,c+y) not in visited:
                        visited.add((r+x,c+y))
                        q.append((r+x,c+y))
        
        def dfs(i,j):
            visited.add((i,j))
            for x,y in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if x in range(m) and y in range(n) and (x,y) not in visited and grid[x][y] =='1':
                    dfs(x,y)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    ans+=1
                    dfs(i,j)
        return ans
        