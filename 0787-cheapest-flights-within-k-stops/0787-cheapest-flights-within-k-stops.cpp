class Solution {

public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> tmp(n);
        this->adj = tmp;
        this->dst = dst;
        vector<bool> visited2(n + 1, false);
        this->visited = visited2;
        
        for (int i = 0; i < flights.size(); i++) {
            adj[flights[i][0]].push_back({flights[i][1], flights[i][2]});
        }
        solve(src, k, 0);
        
        if (fare == INT_MAX) {
            return -1;
        } else {
            return fare;
        }
    }
private:
    int fare = INT_MAX;
    int dst;
    vector<vector<pair<int, int>>> adj;
    vector<bool> visited;
    map<tuple<int, int, int>, bool> dp;
    
    void solve(int src, int k, int cost) {
        if (dp.find({src, k, cost}) != dp.end()) return;
        if (k < -1) return;
        
        if (src == dst) {
            fare = min(fare, cost);
            return;
        }
        
        visited[src] = true;
        for (auto p: adj[src]) {
            if (!visited[p.first] && cost + p.second <= fare) {
                solve(p.first, k - 1, cost + p.second);
            }
        }
        dp[{src, k, cost}] = true;
        visited[src]=false;
        
    }
    
};