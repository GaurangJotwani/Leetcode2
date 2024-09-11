public class Solution {
    public bool ArrayStringsAreEqual(string[] word1, string[] word2) {
        return String.Join("", word1) == String.Join("", word2);
    }
}