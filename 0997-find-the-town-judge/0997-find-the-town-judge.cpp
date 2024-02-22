class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        // [i_trust, trust_me]
        vector<vector<int>> freq(n + 1, vector<int>(2));
        for (auto t: trust) {
            freq[t[0]][0]++;
            freq[t[1]][1]++;
        }
        for (int i = 1; i < n + 1; i++) {
            if (freq[i][0] == 0 && freq[i][1] == n - 1) {
                return i;
            }
        }
        
        return -1;
    }
};