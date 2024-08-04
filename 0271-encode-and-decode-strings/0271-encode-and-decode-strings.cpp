class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encodedString;
        for (string &s : strs) {
            encodedString += to_string(s.size()) + "/:" + s;
        }
        return encodedString;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;
        while (i < s.length()) {
            int delim = s.find("/:", i);
            int len = stoi(s.substr(i, delim - i));
            string str = s.substr(delim + 2, len);
            decoded.push_back(str);
            i = delim + 2 + len;
        }
        return decoded;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));