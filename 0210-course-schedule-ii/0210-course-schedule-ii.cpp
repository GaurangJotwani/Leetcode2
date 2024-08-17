class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> res;
        vector<int> incoming(numCourses, 0);
        vector<vector<int>> adjList(numCourses);
        queue<int> q;

        for (auto pre: prerequisites) {
            adjList[pre[1]].push_back(pre[0]);
            incoming[pre[0]]++;
        }

        for (int i = 0; i < numCourses; i++) {
            if (incoming[i] == 0) q.push(i);
        }

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            res.push_back(node);
            for (auto nei: adjList[node]) {
                incoming[nei]--;
                if (incoming[nei] == 0) q.push(nei);
            }
        }
        if (res.size() == numCourses) return res;
        return {};
    }
};