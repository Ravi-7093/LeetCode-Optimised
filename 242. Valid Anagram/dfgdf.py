def isAnagram():  
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    ans=[]
    nums.remove(pivot)# remove the pivot from the main array
    i=0#Initialize i to zero
	  ans.append(pivot) #append pivot to result array
    for j in nums:# iterate over the elements
		   if j<pivot:# if the current element is less than the pivot 
			    ans.insert(i,j)# insert to the left side of the pivot ie at the beginning of the array
		  	  i=i+1#increment the position 
		   elif j==pivot: #if the element in the array is equal to pivot insert at the middle
		     	ans.insert(i+1,j)
	   	else:
		     	ans.append(j)#if the element in the array is gratear than the pivot insert at the end
	 return ans#return the resultant list
        
