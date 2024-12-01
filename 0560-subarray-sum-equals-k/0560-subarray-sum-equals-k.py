class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        cSum = 0
        res = 0

        for num in nums:
            cSum += num
            if cSum - k in prefix:
                res += prefix[cSum - k]
            prefix[cSum] += 1
        
        return res