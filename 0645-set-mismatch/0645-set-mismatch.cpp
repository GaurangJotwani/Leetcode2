class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_map<int, bool>seen;
        vector<int>res(2);
        for (auto num: nums) {
            if (seen.find(num) != seen.end()) {
                res[0] = num;
                continue;
            }
            seen[num] = true;
        }
        
        for (int i = 1; i < nums.size() + 1; i++) {
            if (seen.find(i) == seen.end()) {
                res[1] = i;
                break;
            }
        }
        
        return res;
    }
};