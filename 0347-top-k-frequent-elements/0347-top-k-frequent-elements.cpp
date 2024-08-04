class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);
        map<int, int> freq;
        for (auto num: nums) freq[num]++;
        for (auto num: freq) buckets[num.second].push_back(num.first);

        vector<int> res;
        for (int i = nums.size(); i >= 0; i--) {
            for (auto num: buckets[i]) {
                res.push_back(num);
                k--;
                if (k == 0) return res;
            }
        }
        return res;
    }
};