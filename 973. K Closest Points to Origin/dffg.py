class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_hp=[]#empty list to form a heap
        res=[]#empty list 
        for x,y in points:
            dis=(x**2)+(y**2)#calculate the distance from the origin 
            min_hp.append([dis,x,y])#append x,y,z to min_hp
        heapq.heapify(min_hp)#convert into heapq so that we can pop lowest values for the size of k 
        while(k>0):
            dis,x,y=heapq.heappop(min_hp)
            res.append([x,y])#append it the result 
            k-=1
        return res#return result
      
      
