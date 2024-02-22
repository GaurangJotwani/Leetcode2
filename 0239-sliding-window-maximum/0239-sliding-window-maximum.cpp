class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<vector<int>> dq;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            while (!dq.empty() && dq.back()[0] < num){
                dq.pop_back();
            }
            dq.push_back({num, i});
            
            
            if (i - dq.front()[1] == k) dq.pop_front();
            
            if (i + 1 >= k){
                res.push_back(dq.front()[0]);
            }
        }
        
        return res;
    }
};