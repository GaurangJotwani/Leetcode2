class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        cSum = 0
        prefix = [0] * len(s)
        prev_lefts = [-1] * len(s)
        previousLeft = -1

        for i,char in enumerate(s):
            prev_lefts[i] = previousLeft
            if char == "|" and previousLeft != -1:
                cSum += i - previousLeft - 1
            if char == "|":
                previousLeft = i
            prefix[i] = cSum
        
        next_right = -1
        next_rights = [-1] * len(s)
        for i in range(len(s) -1, -1, -1):
            next_rights[i] = next_right
            if s[i] == "|":
                next_right = i
        
        print(next_rights)
        print(prev_lefts)

        res = []
        for start,end in queries:
            if s[start] == "*" and next_rights[start] != -1:
                t1 = prefix[next_rights[start]]
            else:
                t1 = prefix[start]
            
            if s[end] == "*" and prev_lefts[end] != -1:
                t2 = prefix[prev_lefts[end]]
            else:
                t2 = prefix[end]
            
            print(t1, t2)
            if t2 > t1:
                res.append(t2 - t1)
            else:
                res.append(0)
        
        print(res)
        return res
