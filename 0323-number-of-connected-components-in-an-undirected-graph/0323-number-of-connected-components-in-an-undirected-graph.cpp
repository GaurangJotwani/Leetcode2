
class DSU {
public:

int comps;
vector<int> parents;
vector<int> ranks;

    DSU(int n) {
        comps = n;
        parents.resize(n);
        for (int i = 0; i < n; i++) parents[i] = i;
        ranks.resize(n, 1);
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
            comps--;
            return true;
        }
        return false;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        for (auto edge: edges) {
            dsu.uni(edge[0], edge[1]);
        }
        return dsu.comps;
    }
};