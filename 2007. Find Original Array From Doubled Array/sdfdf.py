class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        l=0#first pointer to 1st element
        r=1# second pointer to 2nd element 
        result=[]
        changed.sort()#sort the array 
        while(l<len(changed)):#check if l is less than len(array)
            if(r<=l):#check if second pointer is less than right pointer 
                r=l+1#if true increment the second pointer so that second pointer is always greater than right pointer 
            if changed[l] == -1:#check if left pointer pointed element is -1 if true we need to continue 
                l += 1
                continue
            while r < len(changed) and changed[r]!=changed[l]*2: #move r right until it is double of l
                r += 1
            if r==len(changed):#if r is traveresed completely we dont find the element
                return []#return empty result 
            changed[r] = -1 #change the double element founded to -1
            result.append(changed[l])#append the result 
            l += 1#increment first pointer 
        return result#return result
