class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        
        vector<vector<int>> res(2, vector<int>());
        
        map<int, bool> winners;
        map<int, int> losers;
        
        for (auto match: matches) {
            winners[match[0]] = true;
            losers[match[1]]++;
        }
        
        for (auto pair: winners) {
            if(losers.find(pair.first) == losers.end()) {
                res[0].push_back(pair.first);
            }
        }
        
        for (auto pair: losers) {
            if(losers[pair.first] == 1) {
                res[1].push_back(pair.first);
            }
        }
        
        return res;
        
        
    }
};