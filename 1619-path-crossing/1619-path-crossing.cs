public class Solution {
    public bool IsPathCrossing(string path) {
        var history = new HashSet<(int x, int y)>();
        (int x, int y) cPath = (0, 0);
        history.Add((0, 0));

        foreach (var c in path) {
            if (c == 'N') cPath.y += 1;
            else if (c == 'S') cPath.y -= 1;
            else if (c == 'W') cPath.x -= 1;
            else if (c == 'E') cPath.x += 1;
            if (history.Contains(cPath)) return true;
            history.Add(cPath);
        }
        
        return false;
    }
}