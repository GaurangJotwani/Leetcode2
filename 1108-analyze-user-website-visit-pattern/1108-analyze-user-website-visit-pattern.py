class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        scores = defaultdict(set)

        zipped = [(t,u,w) for u,w,t in zip(username, website, timestamp)]
        zipped.sort()
        
        user_act = defaultdict(list)

        for t,u,w in zipped:
            user_act[u].append(w)
        
    
        for key,val in user_act.items():
            for i in range(len(val)):
                for j in range(i + 1, len(val)):
                    for k in range(j + 1, len(val)):
                        pattern = val[i] + "," + val[j] + "," + val[k]
                        scores[pattern].add(key)

        max_len = 0
        output = []
        c_pat = ""
        for key,val in scores.items():
            if len(val) > max_len:
                max_len = len(val)
                c_pat = key
                output = key.split(",")
            elif len(val) == max_len and c_pat > key:
                c_pat = key
                output = key.split(",")

        return output
        
