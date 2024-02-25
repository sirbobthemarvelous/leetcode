class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        s = [0] * (n + 1)
        for i in range(n): s[i + 1] = s[i] + stones[i]
        dp = [[0] * n for _ in range(n)]
        for c in range(2, n + 1):
            for l in range(0, n - c + 1):
                r = l + c - 1
                dp[l][r] = max(s[r + 1] - s[l + 1] - dp[l + 1][r],
                       s[r] - s[l] - dp[l][r - 1])
        return dp[0][n - 1]