class Solution {
public:
    vector<int> res;
    vector<vector<int>> adjList;
    bool dfs(int node, vector<int> &visit) {
        visit[node] = 1;
        for (auto nei: adjList[node]) {
            if (visit[nei] == 1) return false;
            else if (visit[nei] == 0) {
                if (!dfs(nei, visit)) return false;
            }
        }
        visit[node] = 2;
        res.push_back(node);
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adjList = vector<vector<int>>(numCourses);
        vector<int> visit(numCourses, 0);
        for (auto pre: prerequisites) {
            adjList[pre[1]].push_back(pre[0]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (visit[i] == 0) {
                if(!dfs(i, visit)) return false;
            }
        }
        return true;
    }
};