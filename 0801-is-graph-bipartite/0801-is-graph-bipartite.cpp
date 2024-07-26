class Solution {
public:
vector<vector<int>> adjList;

bool dfs(int node, vector<int> &seen, int color) {
    seen[node] = color;
    
    for (auto nei: adjList[node]) {
        if (seen[nei] == 0) {
            if (!dfs(nei, seen, 3 - color)) return false;
        }
        else if(seen[nei] == color) return false;
    }
    
    return true;
}
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
    vector<int> seen(n, 0);
    
    adjList = graph;
    
    for (int i = 0; i < n; i++) {
        if (seen[i] == 0) {
            if (!dfs(i, seen, 1)) return false;
        }
    }
    
    return true;
    }
};