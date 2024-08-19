class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> counts(26, 0);
        for (auto t: tasks) counts[t-'A']++;
        priority_queue<vector<int>, vector<vector<int>>, Comparator> pq; // minHeap
        for (int i = 0; i < 26; i++) {
            if (counts[i] != 0) {
                pq.push({1, counts[i]});
            }
        }
        int t = 0;
        while (!pq.empty()) {
            t++;
            if (pq.top()[0] > t) continue;
            int nxtTime = pq.top()[0] + n + 1;
            int taskLeft = pq.top()[1] - 1;
            cout << nxtTime << " " << taskLeft << endl;
            pq.pop();
            if (taskLeft != 0) pq.push({nxtTime, taskLeft});
        }
        return t;
    }
private:
    struct Comparator {
        bool operator()(vector<int> &v1, vector<int> &v2) {
            return v1[0] > v2[0];
        }
    };
};