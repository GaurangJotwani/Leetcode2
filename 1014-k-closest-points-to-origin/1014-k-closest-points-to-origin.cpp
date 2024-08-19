class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, Comparator>pq;
        for (auto p: points) {
            pq.push({p[0] * p[0] + p[1]*p[1], p[0], p[1]});
            if (pq.size() > k) pq.pop();
        }
        vector<vector<int>> res;
        while (!pq.empty()) {
            res.push_back({pq.top()[1],pq.top()[2]});
            pq.pop();
        }
        return res;
    }

private:
struct Comparator {
    bool operator()(vector<int> &v1, vector<int> &v2) {
        return v1[0] < v2[0];
    }
};
};