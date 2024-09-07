public class Solution {
    public string DestCity(IList<IList<string>> paths) {
        var adjList = new Dictionary<string, List<string>>();
        foreach (var path in paths) {
            var src = path[0];
            var dst = path[1];
            if (adjList.ContainsKey(src)) adjList[src].Add(dst);
            else adjList[src] = new List<string> {dst};
            if (!adjList.ContainsKey(dst)) adjList[dst] = new List<string>();
        }
        foreach(var kvp in adjList) {
            if (kvp.Value.Count == 0) return kvp.Key;
        }

        return "";
    }
}