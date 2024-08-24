class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> res;
        this->separator = separator;
        for (auto w: words) {
            vector<string> listOfWords;
            separate(w, listOfWords);
            for (auto s: listOfWords) res.push_back(s);
        }
        return res;
    }
private:
    char separator;
    void separate(string &word, vector<string> &res) {
        string tmp = "";
        for (char w: word) {
            if (w == separator) {
                if (!tmp.empty()) res.push_back(tmp);
                tmp = "";
            }
            else tmp.push_back(w);
        }
        if (!tmp.empty()) res.push_back(tmp);
    }
};