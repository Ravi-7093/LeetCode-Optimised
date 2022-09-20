# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None#2 pointer approach 
        curr = head# point current to head
        while curr:#traverser until the last node 
            next = curr.next#first ensure to traverse to the next node ie store the link in the next variable 
            #print(next.val)
            curr.next = prev#reverse the pointer to point to prev
            prev = curr#
            print(prev.val)
            curr = next
        return prev#return last node 
        
