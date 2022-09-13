class RecentCounter(object):

    def __init__(self):
        self.lst=[]#create an empty list
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.lst.append(t)#append t value 
        while(self.lst[0]<t-3000): #check if its not inclusive of the range 
            self.lst.pop(0)#pop the value if any 
        return len(self.lst)#return the len of the list 

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
