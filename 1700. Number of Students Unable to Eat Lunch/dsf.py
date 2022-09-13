def countStudents():
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    d={}#create an empty dict
    count=0#let count be initialized to zero
    for i in range(len(students)):
        d[students[i]]=d.get(students[i],0)+1#keep the count of frequencies of 0's and 1's
    print(d)
    for i in sandwiches:#check if d[i] is empty ie no more students are there to eat a particular sandwich
        if d[i]==0:#if true break
            break
        else:
            d[i]=d[i]-1#else decrement the value from the specific sandwich
    print(d)
    for value in d.values():#iterate the values in the dictionary
        count+=value#check the counter
    return count#return the count value
           
           
print(countStudents()) 
