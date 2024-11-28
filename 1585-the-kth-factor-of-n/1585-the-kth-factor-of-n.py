class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        all_factors = []
        i = 1

        while i * i <= n:
            if n % i == 0:
                all_factors.append(i)
                if (n // i != i):
                    all_factors.append(n // i)
            
            i += 1
        
        all_factors.sort()
        print(all_factors)
        if k > len(all_factors): return -1
        return all_factors[k - 1]


