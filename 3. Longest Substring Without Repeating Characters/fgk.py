class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end=0 # intialize the variables to track the boundaries for the longest string with no duplicates
        begin=0
        low=0#intialize the variables to track the boundaries for the window
        high=0
        d={}#take a dictionary
        
        while(high<len(s)):#check if high<len(s)
            if d.get(s[high]):#check if the char in dictionary
                while(s[low]!=s[high]):#if true move the window
                    print(low,high)
                    d[s[low]]=False#make the character value in dictionary to zero
                    low=low+1
                low=low+1#increment the low pointer 
            else:
                d[s[high]]=True#store d's value in dictionary 
                if(end-begin<high-low):#check if end-begin <high-low #to store the boundaries of the longest strin 
                    end=high
                    begin=low
            high=high+1
        res=(s[begin:end+1])#return the len res
        return len(res)
                    
                    
                
                
        
