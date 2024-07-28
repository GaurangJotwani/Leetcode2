class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {

        vector<int> indegrees(numCourses, 0);
        vector<vector<int>> adjList(numCourses);
        vector<int> res;

        for (auto pre: prerequisites) {
            indegrees[pre[0]]++;
            adjList[pre[1]].push_back(pre[0]);
        }

        for (auto &l: adjList) {
            sort(l.begin(), l.end());
        }


        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) q.push(i);
        }

        while(!q.empty()) {
            int node = q.front();
            q.pop();
            res.push_back(node);
            for (auto nei: adjList[node]) {
                indegrees[nei]--;
                if (indegrees[nei] == 0) q.push(nei);
            }
        }

        if (res.size() != numCourses) return vector<int>();

        return res;
        
    }
};