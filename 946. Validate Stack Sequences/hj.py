class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]#created an empty list to perform as a stack
        i=0#intialize i and j to zero
        j=0
        for i in range(len(pushed)):#traverse the arrau
            stack.append(pushed[i])
            while(len(stack)!=0 and stack[-1]==popped[j]):#check if the stack is empty and 
                                                         #the top of the stack to be equal to the element to be pooped in poppedlist
                print(stack,"deleted")
                stack.pop()#pop the elememt if true
                j=j+1#increment the pointer in popped list
        if(len(stack)==0):#check if len(stack) is empty
            return True#return True if stack is empty
        else:
            return False
        
