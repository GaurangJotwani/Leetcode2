class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size();
        int total_xor = 0;
        for (int i = 1; i <= n + 1; i++) {
            total_xor = total_xor ^ i;
        }
        
        for (int i = 0; i < n; i+=2) {
            total_xor = total_xor ^ encoded[i];
        }
        
        int last = total_xor;
        
        vector<int> res;
        res.push_back(last);
        
        for (int i = encoded.size() - 1; i >= 0; i--) {
            last = encoded[i] ^ last;
            res.push_back(last);
        }
        
        reverse(res.begin(), res.end());
        return res;
        
    }
};