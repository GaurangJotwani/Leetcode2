class Solution {
public:
    int longestValidParentheses(string s) {
        
        stack<char> stk1;
        stack<int> stk2; // Stack to store indices of '(' characters
        stk2.push(-1); // Push -1 to handle edge case
        
        int maxLen = 0;
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk1.push('(');
                stk2.push(i);
            } else {
                if (!stk1.empty()) {
                    stk1.pop();
                    stk2.pop();
                    maxLen = max(maxLen, i - stk2.top());
                } else {
                    stk2.push(i);
                }
            }
        }
        
        return maxLen;
    }
};