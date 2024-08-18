class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<pair<int, int>>> adjList(n);
        priority_queue<vector<int>, vector<vector<int>>, Comparator> pq;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int dist = abs(x1 - x2) + abs(y1 - y2);
                adjList[i].push_back({j, dist});
                adjList[j].push_back({i, dist});
            }
        }
        pq.push({0, 0});
        vector<bool> visited(n, false);
        int res = 0;
        while (!pq.empty()) {
            int node = pq.top()[1];
            int w = pq.top()[0];
            pq.pop();
            if (visited[node]) continue;
            visited[node] = true;
            res += w;
            for (auto nei: adjList[node]) {
                if (!visited[nei.first]) {
                    pq.push({nei.second, nei.first});
                }
            }
        }
        return res;



    }
private:
    struct Comparator {
        bool operator()(const vector<int> &v1, vector<int> &v2) {
            return v1[0] > v2[0];
        }
    };
};