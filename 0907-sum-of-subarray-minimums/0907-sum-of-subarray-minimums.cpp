class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        
        long MOD = pow(10, 9) + 7;
        long res = 0;
        stack<pair<long, long>> stk;
        
        for (long i = 0; i < arr.size(); i++) {
            long num = arr[i];
            while (!stk.empty() && num < stk.top().second) {
                pair<long, long> p = stk.top();
                stk.pop();
                long left = !stk.empty() ? p.first - stk.top().first : p.first + 1;
                long right = i - p.first;
                res = (res + p.second * left * right) % MOD;
            }
            
            stk.push({i, num});
        }
        
        
        while (!stk.empty()) {
            pair<long, long> p = stk.top();
            stk.pop();
            long left = !stk.empty() ? p.first - stk.top().first : p.first + 1;
            long right = arr.size() - p.first;
            res = (res + p.second * left * right) % MOD;
            
         }
        
        return res;
        
    }
};

// 3 * 4 + 3 * 3 + 3 * 2 + 3 * 1
// 12 + 9 + 6 + 3