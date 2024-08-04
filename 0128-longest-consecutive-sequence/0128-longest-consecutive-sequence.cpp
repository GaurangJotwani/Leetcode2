class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 1;
        if (nums.size() == 0) return 0;
        unordered_map<int, bool> seen;
        for (auto num: nums) seen[num] = false;

        for (auto num: nums) {
            if (seen[num]) continue;
            seen[num] = true;

            int left = num - 1;
            while (seen.find(left) != seen.end()) {
                seen[left] = true;
                left--;
            }
            int right = num + 1;
            while (seen.find(right) != seen.end()) {
                seen[right] = true;
                right++;
            }
            res = max(res, right - left - 1);
        }
        return res;
    }
};