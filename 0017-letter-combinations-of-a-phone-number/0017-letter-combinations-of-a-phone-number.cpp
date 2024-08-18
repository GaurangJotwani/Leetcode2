class Solution {
public:
    vector<string> res;
    string digits;
    vector<string> mp = {"#", "#", "abc", "def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    void dfs(int idx, string curr) {
        if (idx == digits.size()) {
            res.push_back(curr);
            return;
        }
        int dig = digits[idx] - '0';
        for (auto c: mp[dig]) {
            curr.push_back(c);
            dfs(idx + 1, curr);
            curr.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) return {};
        this->digits = digits;
        dfs(0, "");
        return res;
    }
};