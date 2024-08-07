class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        int n = temperatures.size();
        vector<int> t = temperatures;

        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            while (!stk.empty() && stk.top().second < t[i]) {
                int prevDay = stk.top().first;
                stk.pop();
                result[prevDay] = i - prevDay;
            }
            stk.push({i, t[i]});
        }
        return result;
    }
};