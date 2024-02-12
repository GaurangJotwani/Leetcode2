class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int maj = ceil((float) nums.size() / 2);
        cout  << maj;
        unordered_map<int, int> freq;
        for (auto num: nums) {
            freq[num]++;
            if (freq[num] == maj) {
                return num;
            }
        }
        
        return -1;
        
    }
};