class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minProd = nums[0]
        maxProd = nums[0]
        output = float("-inf")

        for num in nums[1:]:
            if nums == 0:
                minProd, maxProd = 1, 1
                continue
            temp = maxProd
            maxProd = max(num, temp * num, minProd * num)
            minProd = min(num, temp * num, minProd * num)

            output = max(maxProd, output)
        
        return max(output, max(nums))

            

        