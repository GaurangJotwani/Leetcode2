class Solution {
public:
    Solution() {}

    vector<int> par;
    vector<int> sz;

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        par.resize(n);
        sz.resize(n, 1);

        // Initialize each node to be its own parent
        for (int i = 0; i < n; ++i)
            par[i] = i;

        int numComponents = n;

        // Apply Union-Find algorithm
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isConnected[i][j]) {
                    if (uni(i, j)) {
                        // If a union is performed, decrease the component count
                        numComponents--;
                    }
                }
            }
        }
        return numComponents;
    }

private:
    int find(int x) {
        if (par[x] != x)
            par[x] = find(par[x]); // Path compression
        return par[x];
    }

    bool uni(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY) return false; // Already in the same component

        // Union by rank
        if (sz[rootX] < sz[rootY]) {
            par[rootX] = rootY;
            sz[rootY] += sz[rootX];
        } else {
            par[rootY] = rootX;
            sz[rootX] += sz[rootY];
        }

        return true; // A union is performed
    }
};