#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        stack = []#create a stack using a list 
        while head:#
            stack.append(head)#append the values in order to the satck 
            head = head.getNext()#traverse until the last node is reached 
        while stack:
            stack.pop().printValue()#pop the values in the stack
		
