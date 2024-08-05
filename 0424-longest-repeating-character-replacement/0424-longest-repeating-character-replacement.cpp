class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26);
        int i = 0, j = 0, result = 0, maxCount = 0;

        while (j < s.size()) {
            count[s[j] - 'A']++;
            maxCount = max(maxCount, count[s[j] - 'A']);
            if (j - i + 1 - maxCount > k) {
                count[s[i] - 'A']--;
                i++;
            }
            result = max(result, j - i + 1);
            j++;
        }
        return result;

    }
};