# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:#check if trees are empty 
            return True#return True
        if not p or not q or p.val!=q.val:#check if either of them are empty then its false
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))#recursively check if left and right subtree are True
                
        
