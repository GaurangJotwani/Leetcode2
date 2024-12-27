class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        upper = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= upper:
                res.append(True)
            else:
                res.append(False)
        

        return res