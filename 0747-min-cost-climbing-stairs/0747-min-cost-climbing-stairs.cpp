class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        int n = cost.size();
        if (n == 1) return 0;
        vector<int> dp(n + 1);
        int first = 0;
        int second = 0;

        for (int i = 2; i < dp.size(); i++) {
            int res = min(first + cost[i - 2], second + cost[i - 1]);
            first = second;
            second = res;
        }
        return second;

    }
};