class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find pivot index
        int l = 0;
        int r = nums.size() - 1;
        int pivIdx = -1;
        while (l <= r) {
            if (nums[l] <= nums[r]) {
                pivIdx = l; 
                break;
            }
            int mid = l + ((r - l) / 2);
            if (nums[mid] > nums[mid + 1]) {
                pivIdx = mid + 1;
                break;
            }
            if (nums[mid] < nums[mid - 1]) {
                pivIdx = mid;
                break;
            }
            if (nums[mid] >= nums[l]) l = mid + 1;
            else r = mid - 1;
        }
        if (target >= nums[pivIdx] && target <= nums[nums.size() - 1]) {
            l = pivIdx;
            r = nums.size() - 1;
        } else if (target >= nums[0]) {
            l = 0;
            r = pivIdx - 1;
        } else return -1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }


        return -1;

    }
};