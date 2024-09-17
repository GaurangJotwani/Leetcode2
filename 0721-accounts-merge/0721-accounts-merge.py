class Solution:

    def find(self, i, parents):
        if parents[i] == i:
             return i
        parents[i] = self.find(parents[i], parents)
        return parents[i]
    
    def union(self, i, j, parents, ranks, accounts):
        par1 = self.find(i, parents)
        par2 = self.find(j, parents)
        if par1 == par2:
            return None

        email1 = set(accounts[par1][1:])
        email2 = set(accounts[par2][1:])

        if (ranks[par1] > ranks[par2]):
            parents[par2] = par1
            ranks[par1] += ranks[par2]
            accounts[par1] = [accounts[par1][0]] + sorted(list(email1.union(email2)))

        else:
            parents[par1] = par2
            ranks[par2] += ranks[par1]
            accounts[par2] = [accounts[par2][0]] + sorted(list(email1.union(email2)))
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        edges = []
        adjList = defaultdict(list)
        res = []
        parents = [i for i in range(len(accounts))]
        ranks = [1 for i in range(len(accounts))]

        for i in range(len(accounts)):
            account_one_emails = set(accounts[i][1:])
            for j in range(i + 1, len(accounts)):
                account_two_emails = accounts[j][1:]
                for email in account_two_emails:
                    if email in account_one_emails:
                        edges.append([i, j])
                        break
        for edge in edges:
            self.union(edge[0], edge[1], parents, ranks, accounts)
        
        res = []
        for i in range(len(accounts)):
            if (parents[i] == i):
                res.append([accounts[i][0]] + sorted(set(accounts[i][1:])))

        return res



        