class Solution {
    public int swimInWater(int[][] grid) {
        int N = grid.length;
        int lo = 0, hi = N * N - 1;
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            boolean[][] visit = new boolean[N][N];
            if (reachBottom(grid, mi, N, visit, 0, 0)) hi = mi;
            else lo = mi + 1;
        }
        return lo;
    }

    private boolean reachBottom(int[][] grid, int t, int N, boolean[][] visit, int i, int j) {
        if (i < 0 || i >= N || j < 0 || j >= N || visit[i][j] || grid[i][j] > t) return false;
        visit[i][j] = true;
        if (i == N - 1 && j == N - 1) return true;
        else return reachBottom(grid, t, N, visit, i + 1, j) || reachBottom(grid, t, N, visit, i - 1, j) || reachBottom(grid, t, N, visit, i, j - 1) || reachBottom(grid, t, N, visit, i, j + 1);
    }
}