class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left(height.size());
        vector<int> right(height.size());
        
        int left_max = 0;
        int right_max = 0;

        for (int i = 0; i < height.size(); i++) {
            left[i] = left_max;
            right[height.size() - 1 - i] = right_max;
            left_max = max(left_max, height[i]);
            right_max = max(right_max, height[height.size() - 1 - i]);
        }

        int res = 0;
        for (int i = 0; i < height.size(); i++) {
            int temp = min(left[i], right[i]) - height[i];
            if (temp > 0) res += temp;
        }
        return res;
    }
};