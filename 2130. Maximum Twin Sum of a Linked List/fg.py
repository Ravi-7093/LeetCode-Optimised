# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        count=0 #create a counter to get the length
        total_sum=0#check for total sum
        result=0#to store result ie max_sum
        i=0#intialize i to zero
        curr=head#first pointer 
        new_pt=head#second pointer 
        while(curr):#while True
            count+=1#increment the counter 
            curr=curr.next#move the pointer 
        arr=[0]*count#intialoze the array with 0's for the size of the linked list  
        while new_pt.next is not None and i<count:#traverse until the last node
            arr[i]=new_pt.val#store the values in the array
            i=i+1#increment 1
            new_pt=new_pt.next#move the pointer 
        arr[i]=new_pt.val#store the last element value into the array
        print(arr)
        for i in range(len(arr)/2):#to calculate the sum we need to traverse only the first half of the array ie the twin can be identifed 
            print(i)
            total_sum=arr[i]+arr[count-i-1]#using the formula
            if(result<total_sum):#check if result is less than the total_sum
                result=total_sum
        return result#if true return result
        
        
