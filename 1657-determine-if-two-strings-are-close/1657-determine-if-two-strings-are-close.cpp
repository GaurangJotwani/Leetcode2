class Solution {
public:
    bool closeStrings(string word1, string word2) {
        
        if (word1.size() != word2.size()) return false;
        
        vector<int> w1(26, 0);
        vector<int> w2(26, 0);
        vector<int> w11(26, 0);
        vector<int> w22(26, 0);
        
        
        for (auto a:word1) {
            w1[a - 'a']++;
            w11[a - 'a']=1;
        }
        
        for (auto a:word2) {
            w2[a - 'a']++;
            w22[a - 'a']=1;
        }
        
        sort(w1.begin(), w1.end());
        sort(w2.begin(), w2.end());
        
        return w1==w2 && w11==w22;
        
    }
};