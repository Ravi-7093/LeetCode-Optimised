# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        #get a-1 th node and point to list
        #get last node of list point to last node of list 1
        prev=ListNode()
       # new_node=ListNode()
        prev.next=list1
        #
        curr=list1
        #print(curr)
        
        for i in range(a):
            prev =prev.next#move the first pointer until a-1th node
            #print(prev.val)
            curr=curr.next#move the curr pointer until curr node 
            #print(curr.val)
        for i in range(b-a+1):#move until curr is pointing to the next node b 
            curr=curr.next
        prev.next=list2#point the prev pointer to list2 
        while(prev.next):
            prev=prev.next#traverse until last node 
        prev.next=curr #point next node to curr 
        return list1 #return list1
        
            
