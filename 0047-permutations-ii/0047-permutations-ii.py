class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        s = set()
        def helper(curr, remaining):
            if len(curr) == len(nums):
                s.add(tuple(curr))
                return
            
            for i,num in enumerate(remaining):
                curr.append(num)
                helper(curr, remaining[:i] + remaining[i + 1:])
                curr.pop()
        
        
        helper([], nums)
        
        for p in s:
            res.append(list(p))
        
        return res


            


        