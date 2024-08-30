public class Codec {

    private static Dictionary<long, string> idToUrl = new Dictionary<long, string>();
    private static readonly string sixtyTwoBit = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    private static long id = 1;

    // Encodes a URL to a shortened URL
    public string encode(string longUrl) {
        idToUrl[id] = longUrl; 
        return "http://tinyurl.com/" + convertTo62Base(id);
        id++;
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) {
        string[] parts = shortUrl.Split("/");
        long decoded = convertToBase10(parts[parts.Length - 1]);
        return idToUrl[decoded];
    }

    private string convertTo62Base(long i) {
        var sb = new StringBuilder();
        while (i > 0) {
            sb.Append(sixtyTwoBit[(int)(i % 62)].ToString());
            i = i / 62;
        }
        return sb.ToString();
    }

    private long convertToBase10(string s) {
        int res = 0;
        foreach (char c in s) {
            res += res * 62 + sixtyTwoBit.IndexOf(c);
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));