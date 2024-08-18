class Solution {
public:
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adjList(n + 1);
        for (auto time: times) adjList[time[0]].push_back({time[1], time[2]});
        priority_queue<vector<int>, vector<vector<int>>, Comparator> pq;
        pq.push({0, k});
        vector<bool> visited(n + 1, false);
        int res = 0;
        while (!pq.empty()) {
            int node = pq.top()[1];
            int w1 = pq.top()[0];
            pq.pop();
            if (visited[node]) continue;
            visited[node] = true;
            res = max(res, w1);
            for (auto nei: adjList[node]) {
                if (!visited[nei.first]) {
                    pq.push({w1 + nei.second, nei.first});
                }
            }
        }
        for (int i = 1; i <= n; i++) if (!visited[i]) return -1;
        return res;
    }

private:
    struct Comparator {
        bool operator()(const vector<int> &v1, const vector<int> &v2) {
            return v1[0] > v2[0];
        }
    };
};