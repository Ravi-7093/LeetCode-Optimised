# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        frt_pt=head#take first pointer to point to heaf
        sd_pt=head.next#second for traversal for entire list 
        t_sum=0#t_sum to hold the sum inbetween the zero nodes as per the porblem 
        while(sd_pt):#while there are nodes in the linked list
            if sd_pt.val==0:#if the second pointer finds a zero node
                frt_pt=frt_pt.next#move the first pointer to point to next node 
                frt_pt.val=t_sum#store the sum into the first node
                t_sum=0#intialize sumn to zero to get the next nodes sum ehich is present between the nodes
            else:
                t_sum+=sd_pt.val#t_sum is calculated by summing up nodes between the zero nodes  
            sd_pt=sd_pt.next#move the second pointer 
        frt_pt.next=None#make the frt_pt to point none
        return head.next#return the head.next since zero th node is needed
