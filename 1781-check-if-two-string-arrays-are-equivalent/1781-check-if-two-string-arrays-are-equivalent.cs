public class Solution {
    public bool ArrayStringsAreEqual(string[] word1, string[] word2) {
        string s1 = String.Join("", word1);
        string s2 = String.Join("", word2);
        return s1 == s2;
    }
}