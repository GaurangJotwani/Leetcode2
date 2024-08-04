class Solution {
public:
int calcDist(string s1, string s2) {
    for (int i = 1; i < s1.size(); i++) {
        if (s2.find(s1.substr(i)) == 0) {
            return s2.size() - (s1.size() - i);
        }
    }
    return s2.size();
}

int tsp(int currWord, int visited, int n, vector<vector<int>> &dp, vector<vector<int>> &graph, vector<vector<int>> &parent) {
    if (visited == ((1 << n) - 1)) return 0;
    if (dp[currWord][visited] != INT_MAX) return dp[currWord][visited];

    int ans = INT_MAX;
    for (int choice = 0; choice < n; choice++) {
        if ((visited & (1 << choice)) == 0) {
            int sub = graph[currWord][choice] + tsp(choice, visited | (1 << choice), n, dp, graph, parent);
            if (sub < ans) {
                ans = sub;
                parent[currWord][visited] = choice;
            }
        }
    }
    dp[currWord][visited] = ans;
    return ans;
}

string reconstructPath(vector<string> &words, vector<vector<int>> &parent, int start) {
    int n = words.size();
    int visited = 1 << start;
    string result = words[start];
    int curr = start;

    while (true) {
        int next = parent[curr][visited];
        if (next == -1) break;
        result += words[next].substr(words[next].size() - calcDist(words[curr], words[next]));
        visited |= 1 << next;
        curr = next;
    }
    return result;
}
    string shortestSuperstring(vector<string>& words) {
        int n = words.size();
    vector<vector<int>> graph(n, vector<int>(n));
    vector<vector<int>> dp(n, vector<int>(1 << n, INT_MAX));
    vector<vector<int>> parent(n, vector<int>(1 << n, -1));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                graph[i][j] = calcDist(words[i], words[j]);
            }
        }
    }
    
    int ans = INT_MAX;
    int start = 0;
    for (int i = 0; i < n; i++) {
        int temp = tsp(i, 1 << i, n, dp, graph, parent) + words[i].size();
        if (temp < ans) {
            ans = temp;
            start = i;
        }
    }
    
    return reconstructPath(words, parent, start);
    }
};