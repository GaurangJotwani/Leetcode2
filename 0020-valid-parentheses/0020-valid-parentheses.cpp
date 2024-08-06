class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> p = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };
        stack<int> open;

        for (auto c: s) {
            if (p.find(c) != p.end()) {
                // found closing bracket
                if (open.empty()) return false;
                if (open.top() != p[c]) return false;
                open.pop();
            } else open.push(c);
        }

        return open.empty();
    }
};