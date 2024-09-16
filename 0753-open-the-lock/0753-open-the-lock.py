class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s = set(deadends)
        visited = set()
        q = deque()
        visited.add("0000")
        q.append(["0000", 0])

        while q:
            node = q.popleft()
            num, moves = node[0], node[1]
            
            if num == target:
                return moves
            if num in s:  # Skip deadends
                continue
            
            for i in range(4):
                digit = int(num[i])
                
                # Turn the wheel forward
                new_num_forward = num[:i] + str((digit + 1) % 10) + num[i + 1:]
                if new_num_forward not in visited and new_num_forward not in s:
                    q.append([new_num_forward, moves + 1])
                    visited.add(new_num_forward)
                
                # Turn the wheel backward
                new_num_backward = num[:i] + str((digit - 1) % 10) + num[i + 1:]
                if new_num_backward not in visited and new_num_backward not in s:
                    q.append([new_num_backward, moves + 1])
                    visited.add(new_num_backward)
        
        return -1



        

        