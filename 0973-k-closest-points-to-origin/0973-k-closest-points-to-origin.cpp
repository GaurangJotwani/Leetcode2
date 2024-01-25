class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> triples;
        for (auto& point: points) {
            triples.push_back({point[0] * point[0] + point[1] * point[1], point[0], point[1]});
        }
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>>pq(triples.begin(), triples.end());
        vector<vector<int>> res;
        while (k > 0) {
            vector<int> tr = pq.top();
            res.push_back({tr[1],tr[2]});
            pq.pop();
            k--;
        }
        return res;
    }
};