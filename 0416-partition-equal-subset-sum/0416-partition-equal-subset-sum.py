class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2

        seen = set()

        for i in range(len(nums)):
            temp = set()
            temp.add(nums[i])
            for num in seen:
                temp.add(num)
                temp.add(num + nums[i])
            if target in temp:
                return True
            seen = temp
        
        return False


        
        