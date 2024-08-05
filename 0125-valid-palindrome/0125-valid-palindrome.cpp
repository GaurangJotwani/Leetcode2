class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> word;

        for (auto c: s) {
            if ((c <= 'z' && c >= 'a') || (c >= '0' && c <= '9')) {
                word.push_back(c);
            } else if (c >= 'A' && c <= 'Z') {
                word.push_back((c - 'A') + 'a');
            }
        }

        string res(word.begin(), word.end());
        int l = 0;
        int r = res.size() - 1;
        cout << res;

        while (l <= r) {
            if (res[l++] != res[r--]) return false;
        }
        
        return true;
    }
};