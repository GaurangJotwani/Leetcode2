class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for idx, num in enumerate(flowerbed):

            if n == 0:
                return True
            
            if num == 1:
                continue
            
            if idx - 1 >= 0 and flowerbed[idx - 1] == 1:
                continue
            
            if idx + 1 == len(flowerbed) or flowerbed[idx + 1] == 0:
                flowerbed[idx] = 1
                n -= 1
        

        return n == 0

        