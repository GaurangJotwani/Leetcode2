class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> zip;
        for (int i = 0; i < position.size(); i++) zip.push_back({position[i], speed[i]});
        sort(zip.begin(), zip.end(), [](pair<int,int> a, pair<int, int> b) {
            return a > b;
        });
        stack<double> stk;

        for (auto p: zip) {
            double t = ((double)target - (double)p.first) / ((double)p.second);
            stk.push(t);
            if (stk.size() >= 2) {
                double tmp = stk.top();
                stk.pop();
                if (tmp > stk.top()) stk.push(tmp);
            }
        }
        return stk.size();
    }
};