class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>> pq;
        for (auto stone: stones) {
            pq.push(stone);
        }
        
        while(pq.size() > 1) {
            int stone1 = pq.top();
            pq.pop();
            int stone2 = pq.top();
            pq.pop();
            int val = stone1 - stone2;
            if (val != 0) {
                pq.push(val);
            }
        }
        
        return pq.size() == 0 ? 0 : pq.top();
    }
};