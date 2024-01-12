class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        int n = temperatures.size();
        vector<int> result(n);
        
        for (int i = 0; i < n; i++) {
            int currDay = i;
            int currTemp = temperatures[i];
            
            while(!stk.empty() && stk.top().second < currTemp) {
                int prevDay = stk.top().first;
                int prevTemp = stk.top().second;
                stk.pop();
                
                result[prevDay] = currDay - prevDay;
            }
            
            stk.push({currDay, currTemp});
        }
        
        return result;
    }
};