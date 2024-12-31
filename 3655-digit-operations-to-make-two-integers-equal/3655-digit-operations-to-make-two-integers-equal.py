class Solution:
    def minOperations(self, n: int, m: int) -> int:
        primes = set()
        
        for i in range(2, 10001):
            if self.isPrime(i):
                primes.add(i)
        
        if m in primes or n in primes:
            return -1
        
        pq = [(n,n)]
        visited = {}

        while pq:
            c1,n1 = heapq.heappop(pq)
            if n1 == m:
                return c1
            visited[n1] = c1
            for num in self.getNeighbors(n1):
                if num in primes:
                    continue
                if num not in visited or c1 + num < visited[num]:
                    visited[num] = c1 + num
                    heappush(pq, (num + c1, num))

        return -1
        
                  






    def getNeighbors(self, n):
        str_n = str(n)
        nei = []

        for i in range(len(str_n)):
            if str_n[i] != "9":
                new_num = str_n[:i] + chr(ord(str_n[i]) + 1) + str_n[i+1:]
                nei.append(int(new_num))
        
        for i in range(len(str_n)):
            if str_n[i] != "0":
                new_num = str_n[:i] + chr(ord(str_n[i]) - 1) + str_n[i+1:]
                if new_num[0] != "0":
                    nei.append(int(new_num))
        
        return nei





    def isPrime(self, n):

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
