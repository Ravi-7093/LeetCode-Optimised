# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        start=head#initialize the start to point to head 
        st=head#initialize the start to point to head 
        count =0#intialize the count to zero 
        while st:#traverse  until the  last node 
            count+=1#increment the counter 
            st=st.next#
        mid_ele=count//2#calculate the mid element's index
        counter=0#initialize the counter to zero 
        while start:#iterate the linked list 
            if counter==mid_ele:#check if counter is reached the mid element's index
                return start#if true return the start 
            else:
                counter+=1#increment the counter 
                start=start.next#move the start to point to next 
        return None#return None 
