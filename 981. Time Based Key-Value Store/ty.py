class TimeMap(object):

    def __init__(self):
        self.dic={}#create an empty dictionary

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.dic:#check if the given is present in the dictionary
            self.dic[key]=[]#else add key to dictionary 
        self.dic[key].append([value,timestamp])#append the value and timestamp as an array
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res=""#create a variable with empty string res
        values=self.dic.get(key,[])#get the values associated with the key 
        #print(values)
        left=0#left is zero 
        right=len(values)-1#right points to end of list 
        while(left<=right):#doing binary search to get the nearest value associated to the givn timestamp
            mid=(left+right)//2#mid
            if values[mid][1]<=timestamp:#check if values are less than the mid of the array ie less than or equal to timestamp
                print(values[mid][0])
                res=values[mid][0]#result 
                left=mid+1#move the left to point to nextt element 
            else:
                right=mid-1#return the mid-1
        return res#return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
