class Solution {
public:

    int FLIGHT_COUNT;
    unordered_map<string, vector<string>> adjList;
    unordered_map<string, vector<bool>> visited;
    vector<string> result;

    void dfs(string node) {
        for (int i = 0; i < adjList[node].size(); i++) {
            string nei = adjList[node][i];
            if (!visited[node][i]) {
                visited[node][i] = true;
                dfs(nei);
            }
        }

        result.push_back(node);
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        FLIGHT_COUNT = tickets.size();

        for (auto &ticket: tickets) {
            adjList[ticket[0]].push_back(ticket[1]);
        }

        for (auto &l: adjList) {
            sort(l.second.begin(), l.second.end());
            visited[l.first] = vector<bool>(l.second.size(), false);
        }

        dfs("JFK");
        reverse(result.begin(), result.end());
        return result;
    }
};