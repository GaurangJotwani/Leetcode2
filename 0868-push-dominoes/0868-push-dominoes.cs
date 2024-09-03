public class Solution {
    public string PushDominoes(string dominoes) {
        int n = dominoes.Length;
        var sb = new StringBuilder(dominoes);
        var q = new Queue<(char c, int idx)>();
        for (int i = 0; i < n; i++) {
            if (dominoes[i] == 'R') q.Enqueue(('R', i));
            if (dominoes[i] == 'L') q.Enqueue(('L', i));
        }
        var prev = '.';
        var prevIdx = -1;
        while (true) {
            if (q.Count == 0) {
                if (prev == 'R') {
                    for (int i = prevIdx + 1; i < n; i++) {
                        sb[i] = 'R';
                    } 
                }
                break;
             }
             var c_idx = q.Peek().idx;
             var c_char = q.Peek().c;
             if (c_char == 'L') {   
                if (prev == 'L' || prev == '.') for (int j = prevIdx + 1; j < c_idx; j++) sb[j] = 'L';
                else {
                    int dom = ((c_idx - prevIdx - 1) / 2);
                    for (int j = 1; j < dom + 1; j++) {
                        sb[prevIdx + j] = 'R';
                        sb[c_idx - j] = 'L';
                    }
                }
             } 
             else if (prev == 'R') for (int j = prevIdx + 1; j < c_idx; j++) sb[j] = 'R';
             prev = c_char;
             prevIdx = c_idx;
             q.Dequeue();
        }
        return sb.ToString();
    }
}