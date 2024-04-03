class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        
        vector<int> res = {-100000, 100000};
        int max_val = INT_MIN;
        
        for (int i = 0; i < nums.size(); i++) {
            max_val = max(nums[i][0], max_val);
            pq.push({nums[i][0], i, 0});
        }
        while (pq.size() >= nums.size()) {
            int smallest = get<0>(pq.top());
            int lst = get<1>(pq.top());
            int idx = get<2>(pq.top());
            
            if ((max_val - smallest) < (res[1] - res[0])) {
                res[0] = smallest;
                res[1] = max_val;
            }
            pq.pop();
            if (idx == nums[lst].size() - 1) continue;
            max_val = max(nums[lst][idx + 1], max_val);
            pq.push({nums[lst][idx + 1], lst, idx + 1});
            
        }
        
        return res;
    }
};