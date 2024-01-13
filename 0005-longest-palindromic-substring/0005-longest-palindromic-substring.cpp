class Solution {
public:
    string longestPalindrome(string s) {
        int maxStart = 0;
        int maxLength = 1;
        
        for (int i = 0; i  < s.size(); i++) {
            middleout(s, i, i, maxStart, maxLength);
            middleout(s, i, i + 1, maxStart, maxLength);
        }
        
        return s.substr(maxStart, maxLength);
        
    }
    
private:
    void middleout(string s, int i, int j, int& maxStart, int& maxLength) {
        while (i >= 0 && j <= s.size() - 1 && s[i] == s[j]) {
            i--;
            j++;
        }
        
        if (j - i - 1 > maxLength) {
            maxStart = i + 1;
            maxLength = j - i - 1;
        }
    }
};