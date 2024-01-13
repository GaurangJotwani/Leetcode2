class Solution {
public:
    int countSubstrings(string s) {
        int result = 0;
        
        for (int i = 0; i  < s.size(); i++) {
            middleout(s, i, i, result);
            middleout(s, i, i + 1, result);
        }
        
        return result;
    }
    
private:
    void middleout(string s, int i, int j, int& result) {
        while (i >= 0 && j <= s.size() - 1 && s[i] == s[j]) {
            i--;
            j++;
            result++;
        }
    }
};
