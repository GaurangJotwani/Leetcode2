public class Solution {
    public string SimplifyPath(string path) {
        var pathArr = path.Split("/");
        // foreach (var str in pathArr) Console.Write(str + " ");
        // Console.WriteLine();
        // return "/";

        var stk = new Stack<string>();
        foreach (var p in pathArr) {
            if (p == "" || p == ".") continue;
            else if (p == "..") {
                if (stk.Count >= 1) stk.Pop();
            } else stk.Push(p);
        }

        string[] res = stk.ToArray();
        Array.Reverse(res);
        string result = string.Join("/", res);
        return "/" + result; ;
    }
}