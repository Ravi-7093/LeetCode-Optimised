class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub=""
        start=0#Initialize the start to zero
        finalstring=""#result string
        right=len(s) 
        def checkSequence(sub):
            return len(set(sub))//2==len(set(sub.lower()))
        while(right>-1):#iterate until you reach the first character
            while(start<right):#iterate until start<right
                sub=s[start:right]#create a substring
                print(sub)
                bol=checkSequence(sub)#check if the substring satisifes the problem condition
                print(bol)
                if(bol==True) :#check if its True
                    if len(sub) >= len(finalstring):# logic to return the first longest continous sequence
                        finalstring = sub
                    print(finalstring,"finalstring")
                start=start+1#increment the start
            start=0
            right=right-1#decrease the right
        return finalstring#return the final string
