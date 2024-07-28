class Solution {
public:
    vector<int> res;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> adjList(numCourses);
    
    for (auto pre : prerequisites) {
        adjList[pre[1]].push_back(pre[0]);
    }
    
    // Sort each adjacency list to ensure lexicographically smallest order
    for (auto &l : adjList) {
        sort(l.begin(), l.end());
    }
    
    vector<int> visit(numCourses, 0);  // 0: unvisited, 1: visiting, 2: visited
    
    for (int i = 0; i < numCourses; i++) {
        if (visit[i] == 0) {
            if (!dfs(i, adjList, visit)) {
                return vector<int>();  // Return empty vector if a cycle is detected
            }
        }
    }
    
    reverse(res.begin(), res.end());  // Reverse the result to get the correct topological order
    return res;
        
    }
    
    bool dfs(int node, vector<vector<int>> &adjList, vector<int> &visit) {
    visit[node] = 1;  // Mark the node as visiting
    
    for (auto nei : adjList[node]) {
        if (visit[nei] == 1) {
            return false;  // Cycle detected
        } else if (visit[nei] == 0) {
            if (!dfs(nei, adjList, visit)) {
                return false;  // Cycle detected in DFS subtree
            }
        }
    }
    
    visit[node] = 2;  // Mark the node as visited
    res.push_back(node);
    return true;
}
};