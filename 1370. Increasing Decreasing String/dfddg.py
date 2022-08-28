class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        d={}#create a dictionary 
        for i in s:#iterate over the string 
            d[i]=d.get(i,0)+1#calculate the frequency of the characters in the string
        while d:#until the dictionary is empty
            for i in sorted(d.keys()):#iterate the keys  
                if (d[i]>0):#if frequency greater than 0 
                    res+=i#apppend it to the resultant string 
                    d[i]-=1#reduce the frequency by 1
                elif d[i] == 0:#if the frequency of the character becomes 0 pop the character from the dictionary 
                    d.pop(i)
            for i in sorted(d.keys(),reverse=True):#do the same steps as mentioned above in reverse orde 
                if (d[i]>0):
                    res+=i
                    d[i]-=1
                elif d[i] == 0:
                    d.pop(i)
        return res#resultant string 
            
                   
                    
