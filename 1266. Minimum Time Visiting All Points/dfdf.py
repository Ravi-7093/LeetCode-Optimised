class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count=0 #to assign the max value for the distance between x and y coordinates
        total_time=0# total time taken
        for i in range(1,len(points)): 
            x_diff = abs(points[i][0] -points[i-1][0])#check the difference between x co-ordinates  
            y_diff = abs(points[i][1] -points[i-1][1])#check the difference between y co-ordinates  
            if (x_diff>y_diff):#check for  optimal value 
                count = x_diff
            else:
                count  = y_diff
        
            total_time+=count #update the total_time 
         #value_two=i+1[1] - i[1]
         #count += abs(max(value_one,value_two))
        return total_time #return the total_time
