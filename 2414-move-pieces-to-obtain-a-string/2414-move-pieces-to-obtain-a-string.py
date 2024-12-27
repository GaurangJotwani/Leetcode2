class Solution:
    def canChange(self, start: str, target: str) -> bool:
        

        start_q = deque()
        target_q = deque()

        for i,ch in enumerate(start):
            if ch in ("R", "L"):
                start_q.append((ch,i))
        
        for i,ch in enumerate(target):
            if ch in ("R", "L"):
                target_q.append((ch,i))

        if len(start_q) != len(target_q):
            return False

        
        while start_q:
            ch1, idx1 = start_q.popleft()
            ch2, idx2 = target_q.popleft()

            if ch1 != ch2:
                return False
            
            if ch1 == "L":
                if idx2 > idx1:
                    return False
            elif ch1 == "R":
                if idx1 > idx2:
                    return False
        
        return True
            









