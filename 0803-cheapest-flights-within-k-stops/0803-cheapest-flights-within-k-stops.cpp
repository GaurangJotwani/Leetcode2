class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> dp(n, INT_MAX);
        dp[src] = 0;
        for (int i = 0; i <= k; i++) {
            vector<int> tmp = dp;
            for (auto f: flights) {
                int u = f[0];
                int v = f[1];
                int c = f[2];
                if (dp[u] != INT_MAX && dp[u] + c < tmp[v]) {
                    tmp[v] = dp[u] + c;
                }
            }
            dp = tmp;
        }
        if (dp[dst] == INT_MAX) return -1;
        return dp[dst];
    }
};