class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = set()#create an empty set 
        for letter in s:#iterate the string 
            if letter not in ss:#if not in set 
                ss.add(letter)#add the character in the set 
                print(ss)
            else:
                ss.remove(letter)#if present already remove it 
        if len(ss) != 0:#check if the len(ss)
            print(len(s)-len(ss))
            return len(s) - len(ss) + 1 #return the len
        else:
            return len(s)
