class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> stk;
        int res = INT_MIN;

        for (int i = 0; i < heights.size(); i++) {
            int idx = i;
            while (!stk.empty() && heights[i] < stk.top().first) {
                pair<int, int> temp = stk.top();
                stk.pop();
                res = max(res, (i - temp.second)*temp.first);
                idx = temp.second;
            }
            stk.push({heights[i], idx});
        }
        int n = heights.size();
        while(!stk.empty()) {
            pair<int, int> tmp = stk.top();
            stk.pop();
            res = max(res, (n - tmp.second) * tmp.first);
        }
        return res;

    }
};