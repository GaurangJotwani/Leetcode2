class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int lowestSeen = prices[0];

        for (auto p: prices) {
            lowestSeen = min(lowestSeen, p);
            profit = max(profit, p - lowestSeen);
        }
        return profit;
    }
};