class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        p1, p2 = 0, 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            s1,e1 = firstList[p1]
            s2,e2 = secondList[p2]

            #Check if overlap?
            if not (e1 < s2 or e2 < s1):
                res.append([max(s1,s2), min(e1,e2)])
            
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        
        return res
                