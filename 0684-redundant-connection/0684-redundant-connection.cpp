class DSU {
public:
    int n;
    vector<int> parents;
    vector<int> ranks;

    DSU(int n) {
        this->n = n;
        parents.resize(n + 1);
        for (int i = 1; i <=n; i++) parents[i] = i;
        ranks.resize(n + 1, 1);
    }

    int find(int i) {
        if (parents[i] == i) return i;
        return parents[i] = find(parents[i]);
    }

    bool uni(int i, int j) {
        int p1 = find(i);
        int p2 = find(j);
        if (p1 != p2) {
            if (ranks[p1] > ranks[p2]) {
                parents[p2] = p1;
                ranks[p1] += ranks[p2];
            } else {
                parents[p1] = p2;
                ranks[p2] += ranks[p1];
            }
            n--;
            return true;
        }
        return false;
    }



};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        DSU dsu(n);
        for (auto edge: edges) {
            if (!dsu.uni(edge[0], edge[1])) return {edge[0], edge[1]};
        }
        return {};
    }
};