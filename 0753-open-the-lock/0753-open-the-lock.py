class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        q = deque()
        
        deadends =set(deadends)
        if "0000" in deadends:
            return -1
        q.append(([0,0,0,0],0,"0000"))
        visited = set()
        visited.add("0000")

        while q:
            lst,d,key = q.popleft()
            if key == target:
                return d
            for i in range(4):
                new_lst = [num for num in lst]
                new_lst[i] = new_lst[i] + 1 if new_lst[i] != 9 else 0
                key = "".join([str(num) for num in new_lst])
                if key not in visited and key not in deadends:
                    visited.add(key)
                    q.append((new_lst, d + 1, key))

            for i in range(4):
                new_lst = [num for num in lst]
                new_lst[i] = new_lst[i] - 1 if new_lst[i] != 0 else 9
                key = "".join([str(num) for num in new_lst])
                if key not in visited and key not in deadends:
                    visited.add(key)
                    q.append((new_lst, d + 1, key))
        
        return -1
                
            


        