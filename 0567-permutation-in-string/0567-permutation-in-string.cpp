class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        if (m > n) return false;

        vector<int> count(26);
        for (int i = 0; i < m; i++) {
            count[s1[i] - 'a']++;
            count[s2[i] - 'a']--;
        }

        if (isPerm(count)) return true;
        for (int i = m; i < n; i++) {
            count[s2[i] - 'a']--;
            count[s2[i-m] - 'a']++;
            if (isPerm(count)) return true;
        }

        return false;
    }

    bool isPerm(vector<int> &count) {
        for (auto num: count) if (num != 0) return false;
        return true;
    }

};