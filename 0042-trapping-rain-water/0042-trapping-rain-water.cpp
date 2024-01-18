class Solution {
public:
    int trap(vector<int>& height) {
        
        vector<int> left;
        vector<int> right(height.size());
        int maxSeen = 0;
        for (auto num: height) {
            left.push_back(maxSeen);
            maxSeen = max(maxSeen, num);
        }
        
        maxSeen = 0;
        for (int i = height.size() - 1; i >= 0; i--) {
            right[i] = maxSeen;
            maxSeen = max(maxSeen, height[i]);
        }
        
        int result = 0;
        
        for(int i = 0; i < height.size(); i++) {
            int temp = min(left[i], right[i]) - height[i];
            if (temp > 0) result += temp;
        }
        
        return result;
        
        
    }
};