
class DSU {
public:
    int n;
    vector<int> parents;
    vector<int> ranks;
    DSU(int comps) {
        n = comps;
        parents.resize(comps);
        for (int i = 0; i < comps; i++) parents[i] = i;
        ranks.resize(comps, 1);
    }

    int find(int i) {
        if (parents[i] == i) return i;
        return parents[i] = find(parents[i]);
    }
    
    bool uni(int i, int j) {
        int p1 = find(i);
        int p2 = find(j);
        if (p1 == p2) return false;
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
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        for (auto edge: edges) {
            if (!dsu.uni(edge[0], edge[1])) return false;
        }
        return dsu.n == 1;
    }
};