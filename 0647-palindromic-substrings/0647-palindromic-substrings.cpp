class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
           getMaxPalindrome(s, i, i, res);
           getMaxPalindrome(s, i, i + 1, res);
        }
        return res;
    }

private:
    void getMaxPalindrome(string s, int start, int end, int& result) {
        
        while (start >= 0 && end < s.size() && s[start] == s[end]) {
            start -= 1;
            end += 1;
            result++;
        }
    }
};