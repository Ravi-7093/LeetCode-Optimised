class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ret = [0] * k  
        user_acts = {}  
        for log in logs:
            if user_acts.get(log[0], 0):
                user_acts[log[0]].append(log[1])
            else:
                user_acts[log[0]] = [log[1]]
                
        for k, v in user_acts.items():
            l = len(set(v))
            ret[l-1] += 1
    
        return ret
