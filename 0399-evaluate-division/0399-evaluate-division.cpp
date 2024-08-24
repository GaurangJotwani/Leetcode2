class Solution {
public:
    double bfs(string start, string end, unordered_map<string, vector<pair<string, double>>> adjList) {
        unordered_set<string> vis;
        queue<pair<string, double>> q;
        q.push({start, 1});
        vis.insert(start);
        while (!q.empty()) {
            string node1 = q.front().first;
            double wt1 = q.front().second;
            q.pop();
            if (node1 == end) return wt1;
            for (auto nei: adjList[node1]) {
                if (!vis.count(nei.first)) {
                    vis.insert(nei.first);
                    double wt2 = nei.second;
                    q.push({nei.first, wt1 * wt2});
                }
            }
        }
        return -1;
    }

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n = equations.size();
        unordered_map<string, vector<pair<string, double>>> adjList;
        int i = 0;
        for (auto e: equations) {
            adjList[e[0]].push_back({e[1], values[i]});
            adjList[e[1]].push_back({e[0], (((double)1) / values[i])});
            i++;
        }
        vector<double> res;
        for (auto q: queries) {
            if (!adjList.count(q[0]) || !adjList.count(q[1])) {
                res.push_back(-1);
                continue;
            }
            if (q[1] == q[0]) {
                res.push_back(1);
                continue;
            }
            double ans = bfs(q[0], q[1], adjList);
            res.push_back(ans);
        }
        return res;
    }
    
};