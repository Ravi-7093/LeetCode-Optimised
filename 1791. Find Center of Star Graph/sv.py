class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        x,y = edges[0][0], edges[0][1] #store the first node of the edge in  x,  similarly  second in y
        if x==edges[1][0] or x == edges[1][1]: #compare with the next edge ,since if a node is present more than a edge then its the center
             return x
        return y
