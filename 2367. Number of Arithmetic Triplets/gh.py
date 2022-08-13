def arithmeticTriplets():
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        nums = [4,5,6,7,8,9] 
        diff = 2
        count=0
        n = len(nums)
        for i in range(n):
            
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:#we are comparing the values in the reverse order so we are checking 
                                                                     #if the numbers are present or not 
                count += 1
        
        return count
 
#The time complexity of this solution is O(n).
