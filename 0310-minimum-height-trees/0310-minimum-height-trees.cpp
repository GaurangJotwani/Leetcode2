class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0}; // If there's only one node, it's the root of the MHT

        vector<int> in(n, 0);
        vector<vector<int>> adjList(n);

        // Build the graph
        for (auto edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
            in[edge[0]]++;
            in[edge[1]]++;
        }

        // Initialize the first layer of leaves
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (in[i] == 1) q.push(i);
        }

        int remainingNodes = n;

        // Trim the leaves until reaching the centroids
        while (remainingNodes > 2) {
            int leavesCount = q.size();
            remainingNodes -= leavesCount;
            for (int i = 0; i < leavesCount; i++) {
                int leaf = q.front();
                q.pop();
                for (int neighbor : adjList[leaf]) {
                    in[neighbor]--;
                    if (in[neighbor] == 1) q.push(neighbor);
                }
            }
        }

        // Collect the remaining nodes, which are the centroids of the tree
        vector<int> res;
        while (!q.empty()) {
            res.push_back(q.front());
            q.pop();
        }

        return res;
    }
};