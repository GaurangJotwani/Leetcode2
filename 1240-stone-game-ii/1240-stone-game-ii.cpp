class Solution {
public:
    vector<int> piles;
    int n;
    int dp[101][2][101];
    // returns alices stone
    int solve(int M, bool alice, int idx) {
        if (idx == n) return 0;
        if (dp[M][alice][idx] != -1) return dp[M][alice][idx];
        int res = alice ? 0 : INT_MAX;
        int total = 0;
        for (int X = 1; X <= 2 * M; X++) {
            if (idx + X - 1 == n) break;
            total += piles[idx + X - 1];
            if (alice) {
                res = max(res, total + solve(max(M, X) ,!alice, idx + X));
            } else {
                res = min(res, solve(max(M, X), !alice, idx + X));
            }
        }
        cout << res << endl;
        return dp[M][alice][idx] = res;
    }

    int stoneGameII(vector<int>& piles) {
        this->piles = piles;
        n = piles.size();
        memset(dp,-1, sizeof(dp));
        return solve(1, true, 0);
    }
};