class Solution {
public:
    unordered_map<int, bool> visited;
    unordered_map<int, bool> visiting;
    unordered_map<int, vector<int>> adj_list;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (auto v: prerequisites) {
            adj_list[v[0]].push_back(v[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (visited.find(i) == visited.end()) {
                if (!dfs(i)) return false;
            }
        }
        return true;
    }
private:
    bool dfs(int node) {
        if (visiting.find(node) != visiting.end()) return false;
        visiting[node] = true;
        
        for (auto i: adj_list[node]) {
            if (visited.find(i) == visited.end()) {
                if (!dfs(i)) return false;
            }
        }
        
        visiting[node] = false;
        visited[node] = true;
        
        return true;
    }
};