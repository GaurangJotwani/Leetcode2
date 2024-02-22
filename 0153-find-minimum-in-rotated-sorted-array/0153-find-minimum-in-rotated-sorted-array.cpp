class Solution {
public:
    int findMin(vector<int>& nums) {
        int res = nums[0];
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            cout << left << " " << right << "\n";
            if (nums[left] <= nums[right]) {
                res = min(nums[left], res);
                break;
            }
            
            int mid = (left + right) / 2;
            res = min(nums[mid], res);
            
            if (nums[left] <= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return res;
    }
};