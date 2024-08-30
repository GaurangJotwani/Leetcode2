public class Codec {
    private static readonly string alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private Dictionary<string, string> map = new Dictionary<string, string>();
    private Random rand = new Random();

    // Encodes a URL to a shortened URL
    public string encode(string longUrl) {
        string key = GetRand();
        while (map.ContainsKey(key)) key = GetRand();
        map[key] = longUrl;
        return "http://tinyurl.com/" + key;
    }

    private string GetRand() {
        var sb = new StringBuilder();
        for (int i = 0; i < 6; i++) {
            sb.Append(alphabet[rand.Next(62)]);
        }
        return sb.ToString();
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) {
        string key = shortUrl.Replace("http://tinyurl.com/", "");
        return map.ContainsKey(key) ? map[key] : null;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));