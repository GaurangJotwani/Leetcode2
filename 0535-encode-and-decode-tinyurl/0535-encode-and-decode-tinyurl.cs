public class Codec {

    private static Dictionary<int, string> idToUrl = new Dictionary<int, string>();
    private static readonly Dictionary<int, char> base16 = new Dictionary<int, char> {
        {0, '0'},
        {1, '1'},
        {2, '2'},
        {3, '3'},
        {4, '4'},
        {5, '5'},
        {6, '6'},
        {7, '7'},
        {8, '8'},
        {9, '9'},
        {10, 'A'},
        {11, 'B'},
        {12, 'C'},
        {13, 'D'},
        {14, 'E'},
        {15, 'F'},
    };

    private static readonly Dictionary<char, int> base16Rev = new Dictionary<char, int> {
        {'A', 10},
        {'B', 11},
        {'C', 12},
        {'D', 13},
        {'E', 14},
        {'F', 15},
    };

    private static int id = 1;

    // Encodes a URL to a shortened URL
    public string encode(string longUrl) {
        idToUrl[id] = longUrl; 
        return "http://tinyurl.com/" + convertTo16Base(id);
        id++;
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) {
        string[] parts = shortUrl.Split("/");
        int decoded = convertToBase10(parts[parts.Length - 1]);
        return idToUrl[decoded];
    }

    private string convertTo16Base(int i) {
        var sb = new StringBuilder();
        while (i > 0) {
            sb.Append(base16[i % 16].ToString());
            i = i / 16;
        }
        return sb.ToString();
    }

    private int convertToBase10(string s) {
        int res = 0;
        foreach (char c in s) {
            if (base16Rev.ContainsKey(c)) res += res * 16 + base16Rev[c];
            else res += res * 16 + int.Parse(c.ToString());
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));