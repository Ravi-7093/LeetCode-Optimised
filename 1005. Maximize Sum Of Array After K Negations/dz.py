class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() #sort the numbers
        i = 0
        while i < len(nums) and nums[i] < 0 and k > 0:#check for len(nums) and nums[i]<0
            k -= 1#reduce the k vlaue by one 
            nums[i] *= -1 #change the least value to positive number 
            i += 1 #increment i 
        if k % 2 == 0:#check if k is positive 
            return sum(nums) #return sum
        else:
            return sum(nums) - 2*min(nums)#return sum 
                
