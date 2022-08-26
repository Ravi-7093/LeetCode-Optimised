class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        cap=capacity#store the water capacity to new variable
        steps=0#intialize the steps to zero
        for i in range(len(plants)):#iterate over the list 
            if(plants[i]<=cap):#if the watering plant value is less than capacity 
                steps+=1#move one step forward from the river
                cap-=plants[i]#reduce the capacity of the water 
            else:
                cap=capacity#else capacity 
                cap-=plants[i]#reduce the capcity by plant value
                steps+=(2*i)+1#double the steps and add 1
        return steps#return the steps
            
