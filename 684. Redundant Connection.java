class Solution {
    class UnionFind {
        int[] parent;
        int[] rank;
        int size;

        public UnionFind(int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
            rank = new int[size];
            this.size = size;
        }

        public int find(int x) {
            if (parent[x] != x) {
                 parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public boolean union(int x, int y) {
            int xp = find(x);
            int yp = find(y);
            if (xp == yp) {
                return false;
            }
            if (rank[xp] < rank[yp]) {
                parent[xp] = yp;
            } else if (rank[xp] > rank[yp]) {
                parent[yp] = xp;
            } else {
                parent[yp] = xp;
                rank[xp]++;
            }

            return true;
        }
    }
    public int[] findRedundantConnection(int[][] edges) {
        //  int N = 1001;
        int N = edges.length;
        UnionFind uf = new UnionFind(N);
        for (int[] edge: edges) {
            if (!uf.union(edge[0] - 1, edge[1] - 1)) {
                return edge;
            }
        }
        return new int[0];
    }

}