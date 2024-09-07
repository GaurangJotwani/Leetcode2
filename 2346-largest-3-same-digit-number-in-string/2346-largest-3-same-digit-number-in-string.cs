public class Solution {
    public string LargestGoodInteger(string num) {

        var res = "";

        for (int i = 0; i <= num.Length - 3; i++) {
            var cString = num.Substring(i, 3);
            if (IsUnique(cString) && (res == "" || cString[0] > res[0])) res = cString;
        }

        return res;
    }

    private bool IsUnique(string s) {
        var seen = new HashSet<char>();
        foreach (var c in s)seen.Add(c);
        return seen.Count == 1; 
    }
}