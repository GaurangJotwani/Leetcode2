class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        if (nums.size() == 0) return 0;
        
        int res = 1;
        unordered_map<int, bool>seen;
        for (auto num: nums) {
            seen[num] = false;
        }
        
        for (auto num: nums) {
            
            if (seen[num] == true) continue;
            seen[num] = true;
            
            int left = num - 1;
            while (seen.find(left) != seen.end()) {
                seen[left] = true;
                left -= 1;
            }
            
            int right = num + 1;
            while (seen.find(right) != seen.end()) {
                seen[right] = true;
                right += 1;
            }
            res = max(res, right - left - 1);
        }
        
        return res;
    }
};