class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (auto token: tokens) {
            if (token.size() > 1 || isdigit(token[0])) {
                stk.push(stoi(token));
                continue;
            }

            int num2 = stk.top();
            stk.pop();
            int num1 = stk.top();
            stk.pop();
            int result;
            if (token == "+") result = num1 + num2;
            if (token == "-") result = num1 - num2;
            if (token == "*") result = num1 * num2;
            if (token == "/") result = num1 / num2;
            stk.push(result);
        }
        return stk.top();
    }
};