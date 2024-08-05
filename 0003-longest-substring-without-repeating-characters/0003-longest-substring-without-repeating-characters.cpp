class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int j = 0;
        int result = 0;
        unordered_set<int> mp;

        while (j < s.length()) {
            if (mp.find(s[j]) == mp.end()) {
                result = max(result, j - i + 1);
                mp.insert(s[j++]);
            } else {
                mp.erase(s[i++]);
            }
        }
        return result;
    }
};