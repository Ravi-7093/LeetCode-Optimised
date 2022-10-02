class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if(sum(gas)<sum(cost)):#check if total sum of gas < total sum of cost
            return -1
        
        total=0#total is zero 
        start=0#start is zero 
        
        for i in range(len(gas)):#iterate over the array
            total+=(gas[i]-cost[i])#check if total <0
            print(total)
            if total <0:
                total=0
                start=i+1#increment the position 
        return start#return index
            
