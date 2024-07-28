class Solution {
public:
    int res = 0;

    int dfs(int node, vector<bool> &visiting, vector<bool> &visited, vector<vector<int>> &adjList, vector<vector<int>> &counts, string &colors) {
        if (visiting[node]) return INT_MAX;
        if (visited[node]) return counts[node][colors[node] - 'a'];

        visiting[node] = true;

        for (auto nei: adjList[node]) {
            if (dfs(nei, visiting, visited, adjList, counts, colors) == INT_MAX) return INT_MAX;
            for (int i = 0; i < 26; i++) {
                counts[node][i] = max(counts[node][i], counts[nei][i]);
            }
        }
        counts[node][colors[node] - 'a']++;
        res = max(counts[node][colors[node] - 'a'], res);
        visiting[node] = false;
        visited[node] = true;

        return counts[node][colors[node] - 'a'];
    }

    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        vector<vector<int>> adjList(n);
        vector<bool> visiting(n, false);
        vector<bool> visited(n, false);
        vector<vector<int>> counts(n, vector<int>(26));
        for (auto edge: edges) {
            adjList[edge[0]].push_back(edge[1]);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, visiting, visited, adjList, counts, colors) == INT_MAX) return -1;
            }
        }
        return res;
    }
};