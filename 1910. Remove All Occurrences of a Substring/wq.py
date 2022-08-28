class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        res=""#result string 
        index=0#intial index is zero
        for i in range(len(s)):#iterate the string 
            res+=s[i]#append the character to the resultant string 
            while(len(res)>=len(part)):#check if length of resultant array is equal to length of the part
                index = len(res)-len(part)#calculate the index 
                if(res[index:]==part):#check if the resultant list is equal to the part 
                    temp=res[:index]#append the characters before the index from the resultant array
                    res=temp#move it to resultant string 
                else:
                    break
        return res#return the resultant string 
                    
            
