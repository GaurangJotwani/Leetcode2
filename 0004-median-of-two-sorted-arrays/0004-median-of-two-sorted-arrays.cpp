class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        return solve(nums1, nums1.size(), nums2, nums2.size());
    }
private:
    double solve(vector<int>& nums1, int n, vector<int>& nums2, int m) {
        
        if (n > m) return solve(nums2, m, nums1, n);
        
        int low = 0;
        int high = n;
        int partSize = (n + m + 1) / 2;
        
        while (low <= high) {
            int partX = (low + high) / 2;
            int partY = partSize - partX;
            
            int maxLeftX = partX == 0 ? INT_MIN : nums1[partX - 1];
            int minRightX = partX == n ? INT_MAX : nums1[partX];
            
            int maxLeftY = partY == 0 ? INT_MIN : nums2[partY - 1];
            int minRightY = partY == m ? INT_MAX : nums2[partY];
            
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((m + n) % 2 == 0) {
                    return (double(max(maxLeftX, maxLeftY) + double(min(minRightX, minRightY)))/2);
                } else {
                    return double(max(maxLeftX, maxLeftY));
                }
            } else if (maxLeftX > minRightY) 
                high = partX - 1;
            else {
                low = partX + 1;
            }
            
        }
        
        return double(0);
    } 
};