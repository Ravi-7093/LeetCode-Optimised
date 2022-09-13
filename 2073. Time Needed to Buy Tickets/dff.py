import math
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        res=0#intialize the sum to zero 
        for i in range(len(tickets)):#iterate the tickets 
            if (i<=k):#check for the values before kth pos
                res=res+min(tickets[k],tickets[i])#get the minimum tickets collected by each person before reaching kth pos (since at each pass we are collecting tickets until k is 0)
            else:
                res=res+min(tickets[k]-1,tickets[i])#for k+1 pos we iterate until k is zero so we consider k-1 value (important logic)
        return res #return the result
