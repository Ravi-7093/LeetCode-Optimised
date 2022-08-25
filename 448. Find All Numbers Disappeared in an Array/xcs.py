class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp=abs(nums[i])-1 #calculate the index 
            if(nums[temp]>0):#check if the number present at the index is greater than 0 
                nums[temp]*=-1##negate the number 
        res=[]
        for i,n in enumerate(nums):
            if(n>0):
                res.append(i+1)#append the values of i to resultant array
        return res
