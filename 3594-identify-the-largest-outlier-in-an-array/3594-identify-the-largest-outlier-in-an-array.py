class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:


        total_sum = sum(nums)
        cnts = Counter(nums)
        res = float("-inf")

        for outlier in nums:
            if (total_sum - outlier) % 2 == 1:
                continue
            
            S = (total_sum - outlier) // 2
            
            if S not in cnts or (S == outlier and cnts[S] == 1):
                continue
            
            res = max(res, outlier)

        
        return res
            
