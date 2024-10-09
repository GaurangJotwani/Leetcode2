class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_to_odd_indices(s: str, a: int) -> str:
            # Add `a` to all odd indices, cycling back from 9 to 0
            chars = list(s)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            return ''.join(chars)

        def rotate_string(s: str, b: int) -> str:
            # Rotate the string by `b` positions to the right
            return s[-b:] + s[:-b]
        
        visited = set([s])
        queue = deque([s])
        smallest = s
        
        while queue:
            current = queue.popleft()
            
            # Update the smallest lexicographic string
            smallest = min(smallest, current)
            
            # Apply the "add to odd indices" operation
            transformed_add = add_to_odd_indices(current, a)
            if transformed_add not in visited:
                visited.add(transformed_add)
                queue.append(transformed_add)
            
            # Apply the "rotate by b" operation
            transformed_rotate = rotate_string(current, b)
            if transformed_rotate not in visited:
                visited.add(transformed_rotate)
                queue.append(transformed_rotate)
        
        return smallest