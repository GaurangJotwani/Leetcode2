class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int res = INT_MAX;
        int high = *max_element(piles.begin(), piles.end());
        int low = 1;
        
        while (low <= high) {
            int speed = low + ((high - low) / 2);
            double hours = 0;
            for (int i = 0; i < piles.size(); i++) {
                hours += ceil(((double)piles[i]) / speed);
            }
            if (hours <= h) {
                res = min(speed, res);
                high = speed - 1;
            } else low = speed + 1;
        }
        return res;

    }
};