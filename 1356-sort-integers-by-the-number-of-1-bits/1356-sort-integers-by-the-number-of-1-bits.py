class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        res = []
        for num in arr:
            res.append((self.countOneBits(num), num))
        res.sort()
        
        output = []
        for bit, num in res:
            output.append(num)
        
        return output
            
        
        
    
    def countOneBits(self, num):
        
        count = 0
        while num != 0:
            if num & 1 != 0:
                count += 1
            
            num = num >> 1
        
        return count
                
            
            
        