class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)
        res = []
        for i in range(0, 2**n):
            tmp = []

            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        
        return res
