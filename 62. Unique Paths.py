class Solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
        
        """
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m>n):
            bigger = m
            smaller = n
        else:
            bigger = n
            smaller = m
        total = 0
        for x in range(smaller):
            total += bigger - x
        return total """