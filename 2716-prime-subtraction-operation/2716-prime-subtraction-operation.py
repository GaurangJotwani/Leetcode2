class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        list_of_primes = [0]
        for i in range(2, 1001):
            if self.isPrime(i):
                list_of_primes.append(i)
        
        for i, num in enumerate(nums):
            lower = nums[i - 1] if i - 1 >= 0 else float("-inf")
            for prime in list_of_primes:
                if prime >= num or num - prime <= lower:
                    break
                nums[i] = num - prime

            if nums[i] <= lower:
                return False
                
        return True
        

    
    def isPrime(self, num):
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

