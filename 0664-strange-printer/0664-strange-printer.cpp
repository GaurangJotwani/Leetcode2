class Solution {
public:
    int strangePrinter(string s) {
        s = removeDup(s);
        int n = s.length();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        return minTurns(0, n-1, s, memo);
    }
    int minTurns(int start, int end, string&s, vector<vector<int>> &memo) {
        if (start > end) return 0;

        if (memo[start][end] != -1) return memo[start][end];

        int minT = 1 + minTurns(start + 1, end, s, memo);

        for (int k = start + 1; k <= end; k++) {
            if (s[k] == s[start]) {
                int t = minTurns(start, k - 1, s, memo) + minTurns(k + 1, end, s, memo);
                minT = min(minT, t); 
            }
        }
        return memo[start][end] = minT;
    }

    string removeDup(string &s) {
        string uniqueChars;
        int i = 0;
        while (i < s.length()) {
            char curr = s[i];
            uniqueChars += curr;
            while (i < s.length() && s[i] == curr) i++;
        }
        return uniqueChars;
    }
};