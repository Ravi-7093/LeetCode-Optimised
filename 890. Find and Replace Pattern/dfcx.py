class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def get_pattern(s):
            lookup={}#create an empty dictionary 
            output=[]#create an empty list
            i=0#i=0
            for c in s:#traverse the string 
                if c in lookup:#check if the character is present in the dictionary 
                    output.append(lookup[c])#append the value to create a pattern
                else:
                    i+=1#increment the counter 
                    lookup[c]=i#append value in lookup if character not present 
                    output.append(i)#append the value to the list 
            return output
        p = get_pattern(pattern)
        output=[]
        for word in words:# iterate each word
            if get_pattern(word)==p:#check if the pattern of each word  is equal to the pattern of the string 
                    output.append(word)#append the list 
        return output
