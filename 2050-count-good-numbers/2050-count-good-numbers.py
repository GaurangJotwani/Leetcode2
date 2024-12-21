class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10 ** 9 + 7
        if n % 2 == 0:
            return self.binaryExpo(20, n // 2, mod)
        else:
            return (self.binaryExpo(5, (n // 2) + 1, mod) * self.binaryExpo(4, (n // 2), mod)) % mod
        
        
        
    
    def binaryExpo(self, a, b, mod):

        ans = 1
        while b:
            if b & 1 == 1:
                ans = (ans * a) % mod
            a = (a * a) % mod
            b = b // 2
        return ans % mod


        