class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        cnts = defaultdict(int)
        mod = 10 ** 9 + 7
        word_len = len(words[0])
        
        for i in range(word_len):
            for word in words:
                cnts[(i, word[i])] += 1
        
        cache = {}
        
        
        def dfs(idx, level):
            if len(target) == idx:
                return 1
            if level >= word_len:
                return 0
            
            if (idx, level) in cache:
                return cache[(idx, level)]

            total = 0

            total = ((dfs(idx, level + 1) % mod) + total ) % mod

            c_char = target[idx]

            if (level, c_char) in cnts:
                freq = cnts[(level, c_char)]
                total += (freq * dfs(idx + 1, level + 1)) % mod
            
            cache[(idx,level)] = total % mod
            return total % mod
        


        return dfs(0,0)