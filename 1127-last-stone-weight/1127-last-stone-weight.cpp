class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>> pq;
        for (auto s: stones) pq.push(s);
        while (pq.size() > 1) {
            int max1 = pq.top();
            pq.pop();
            int max2 = pq.top();
            pq.pop();
            int diff = max1 - max2;
            if (diff != 0) pq.push(diff);
        }
        if (pq.empty()) return 0;
        return pq.top();
    }
};