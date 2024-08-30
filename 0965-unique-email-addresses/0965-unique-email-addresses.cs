public class Solution {
    public int NumUniqueEmails(string[] emails) {
        var seen = new HashSet<string>();
        int cnt = 0;
        foreach(var email in emails) {
            var s = processEmail(email);
            if (!seen.Contains(s)) cnt++;
            seen.Add(s);
        }
        return cnt;
    }

    private string processEmail(string email) {
        string[] s = email.Split("@");
        var sb = new StringBuilder("");
        foreach (char c in s[0]) {
            if (c == '.') continue;
            if (c == '+') break;
            sb.Append(c);
        }
        return sb.Append("@" + s[1]).ToString();
    }
}