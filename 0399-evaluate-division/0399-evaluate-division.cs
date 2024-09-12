public class Solution {
    private Dictionary<string,List<(string c,double w)>> adj;

    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) {
        adj = new Dictionary<string,List<(string c,double w)>>();
        int i = 0;
        foreach (var eq in equations) {
            double wt = values[i++];
            string src = eq[0];
            string dst = eq[1];

            if (!adj.ContainsKey(src)) adj[src] = new List<(string c, double w)>();
            if (!adj.ContainsKey(dst)) adj[dst] = new List<(string c, double w)>();

            adj[src].Add((dst, wt));
            adj[dst].Add((src, 1 / wt));
        }
        var res = new double[queries.Count];

        i = 0;
        foreach (var q in queries) {
            if (!adj.ContainsKey(q[0]) || !adj.ContainsKey(q[1])) res[i++] = -1;
            else if (q[0] == q[1]) res[i++] = 1;
            else res[i++] = bfs(q[0], q[1]);
        }
        return res;
    }

    public double bfs(string src, string dst) {
        var q = new Queue<(string c, double w)>();
        var visited = new HashSet<string>();
        visited.Add(src);
        q.Enqueue((src, 1));
        while (q.Count != 0) {
            var node = q.Dequeue();
            if (node.c == dst) return node.w;
            foreach (var nei in adj[node.c]) {
                if (!visited.Contains(nei.c)) {
                    visited.Add(nei.c);
                    q.Enqueue((nei.c, node.w * nei.w));
                }
            }
        }
        return -1;
    }









}