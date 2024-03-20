class Solution {
public:
    vector<int> par;
    vector<int> rnk;
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        par = vector<int>(n + 1);
        rnk = vector<int>(n + 1, 1);
        
        for (int i = 0; i < n + 1; i++) {
            par[i] = i;
        }
        
        for (auto edge: edges) {
            if (!uni(edge[0], edge[1])) {
                return edge;
            }
        }
        
        return edges[0];
    }
    
private:
    bool uni(int i, int j) {
        int p1 = find(i);
        int p2 = find(j);
        if (p1 == p2) return false;
        
        if (rnk[p1] > rnk[p2]) {
            par[p2] = p1;
            rnk[p1] += rnk[p2];
        } else {
            par[p1] = p2;
            rnk[p2] += rnk[p1];
        }
        
        return true;
    }
    
    int find(int i) {
        int res = i;
        while (res != par[res]) {
            res = par[res];
        }
        return res;
    }
};