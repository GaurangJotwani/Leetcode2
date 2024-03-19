class Solution {
public:
    unordered_map<int, bool> visited;
    unordered_map<int, bool> visiting;
    stack<int> stk;
    unordered_map<int, vector<int>> adj_list;
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<int> res;
        
        for (auto v: prerequisites) {
            adj_list[v[1]].push_back(v[0]);
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (visited.find(i) == visited.end()) {
                if (!dfs(i)) return vector<int>(); // If cycle detected during DFS, return empty vector
            }
        }
        
        while (!stk.empty()) {
            res.push_back(stk.top());
            stk.pop();
        }
        
        return res;
        
    }
    
    bool dfs(int node) {
        if (visiting[node]) return false; // If the node is already being visited, cycle detected
        
        visiting[node] = true; // Mark as being visited
        
        for (auto i: adj_list[node]) {
            if (!visited[i]) { // If the node is not visited, continue DFS
                if (!dfs(i)) return false; // If cycle detected further down the DFS path, propagate it upwards
            }
        }
        
        visiting[node] = false; // Mark as not being visited
        visited[node] = true; // Mark as visited
        stk.push(node);
        
        return true; // No cycle detected
    }
};