class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0 #counter to count 1's
        while n: #while n is not zero
            n&=n-1 #bitwise and technique to remove 1's
            res+=1 #increment res to hold 1's
        return res #return result
