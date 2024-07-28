class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int nodeCount = colors.size();
        int nodeSeen = 0;
        int res = 0;
        vector<vector<int>> adjList(nodeCount);
        vector<int> inDegrees(nodeCount, 0);

        for(auto &edge: edges) {
            adjList[edge[0]].push_back(edge[1]);
            inDegrees[edge[1]]++;
        }
        vector<vector<int>> counts(nodeCount, vector<int>(26, 0));
        queue<int> q;
        for (int i = 0; i < inDegrees.size(); i++) {
            if (inDegrees[i] == 0) q.push(i);
        }
        while(!q.empty()) {
            int node = q.front();
            q.pop();
            counts[node][colors[node] - 'a']++;
            res = max(counts[node][colors[node] - 'a'], res);
            nodeSeen++;
            for (auto &nei: adjList[node]) {
                for (int i = 0; i < 26; i++) {
                    counts[nei][i] = max(counts[nei][i], counts[node][i]);
                }
                inDegrees[nei]--;
                if (inDegrees[nei] == 0) q.push(nei);
            }
        }

        if (nodeSeen != nodeCount) return -1;
        return res;
    }
};