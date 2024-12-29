class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        times = defaultdict(int)

        stk = []

        for log in logs:
            f_id, start, timestamp = log.split(":")
            f_id = int(f_id)
            timestamp = int(timestamp)
            if start == "start":
                if stk:
                    func_id, s_time = stk[-1]
                    times[func_id] += timestamp - s_time
                stk.append([f_id, timestamp])
            else:
                s_time = stk[-1][1]
                times[f_id] += timestamp - s_time + 1
                stk.pop()
                if stk:
                    stk[-1][1] = timestamp + 1
            
            # print(log, " - " ,times)
            # print(stk)
        
        # print(times)
        res = [0] * n
        for i in range(n):
            res[i] = times[i]
        return res

        