class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        int len = s.size();
        int n = words[0].size();
        int m = words.size();
        int windowSize = n * m;
        
        unordered_map<string, int> freq, curr;
        
        for (auto s: words) {
            freq[s]++;
        }
        
        vector<int> ans;
        
        for (int startPos = 0; startPos < n; startPos++) {
            int start = startPos;
            do {
                curr = freq;
                string currWord;
                bool matched = true;
                
                for (int i = 0; i < m; i++) {
                    currWord = s.substr(start + i * n, n);
                    if (!curr.count(currWord) or curr[currWord] == 0) {
                        matched = false;
                        break;
                    }
                    curr[currWord]--;
                }
                
                if (matched == true) {
                    ans.push_back(start);
                }
                
                start += n;
                
            } while(start + windowSize - 1 < len);
            
        }
        
        return ans;
        
        
    }
};