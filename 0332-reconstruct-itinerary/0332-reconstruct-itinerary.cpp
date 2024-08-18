class Solution {
public:
    vector<string> res;
    
    void postOrderDfs(string node, unordered_map<string, vector<string>> &adjList, unordered_map<string, int> &outgoing) {
        cout << node << " " << outgoing[node] << endl;
        while (outgoing[node] > 0) {
            outgoing[node]--;
            postOrderDfs(adjList[node][outgoing[node]], adjList, outgoing);
        }
        res.push_back(node);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> adjList;
        unordered_map<string, int> outgoing;
        for(auto ticket: tickets) {
            adjList[ticket[0]].push_back(ticket[1]);
            outgoing[ticket[0]]++;
        };
        for (auto &l: adjList) {
            sort(l.second.begin(), l.second.end());
            reverse(l.second.begin(), l.second.end());
        };
        
        postOrderDfs("JFK", adjList, outgoing);

        reverse(res.begin(), res.end());
        return res;

    }
};