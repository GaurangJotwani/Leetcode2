class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjList = defaultdict(set)
        all_chars = set(''.join(words))
        
        # Step 2: Build the adjacency list
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # Check for prefix order violation
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break  # Only consider the first differing character
        
        # Step 3: Topological sort using DFS
        visiting = set()
        visited = set()
        res = []
        
        def dfs(node):
            visiting.add(node)
            
            for nei in adjList[node]:
                if nei in visited:
                    continue
                if nei in visiting:
                    return False
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        # Perform DFS for all characters
        for char in all_chars:
            if char not in visited:
                if not dfs(char):
                    return ""
        
        # Reverse result to get the correct order
        res.reverse()
        return "".join(res)