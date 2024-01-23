class Solution {
public:
    vector<string> letterCombinations(string digits) {
         
        unordered_map<char, string>mp = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> result;
        if (digits.empty()) return result;
        string curr = "";
        helper(0, curr, digits, mp, result);
        return result;
    }
private:
    void helper(int idx, string curr, string& digits, unordered_map<char, string>& mp, vector<string>& result) {
        if (idx == digits.size()) {
            result.push_back(curr);
            return;
        }
        
        for (auto c: mp[digits[idx]]) {
            string s = curr + c;
            helper(idx + 1, s, digits, mp, result);
        }
        
    }
};