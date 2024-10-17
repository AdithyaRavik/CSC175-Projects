
 

#Purpose: Validates the input and adds togther only the numbers 
#Input: arguments alist
#Output: returns a new list that has only numbers in it
#Assumptions: input is an integer, float, or string 
def input_validation(alist):
    new_alist = []
    for z in alist:

        if isinstance(z,int) or isinstance(z,float):
            new_alist = new_alist + [z]
    return(new_alist)


#Purpose: Determines the maximum value in list
#Input: argument alist
#Output: returns the maximum value
#Assumptions: input for argument are numbers
def max_value(alist):

    val = alist[0]
    for x in alist:
        if val < x:
            val = x
    return val
    
#Purpose: Finds the minimum value in list
#Input: argument alist
#Output: returns the minimum value
#Assumptions: input for argument are numbers
def min_value(alist):
    val2 = alist[0]
    for y in alist:
        if val2 > y:
            val2 = y
    return val2

#Purpoe: Removes one occurance of the maximum and minimum values in the list
#Input: argument value
#Output: return new list value with one occurance of max and min removed
#Assumptions: input for argument are numbers
def remove_num(value):

    total_num = []

    valid = input_validation(value)

    abs_max = max_value(valid)
    abs_min = min_value(valid)

    e = valid.index(abs_max)
    f = valid.index(abs_min)
    
    for x in range(len(valid)):
        if x != e and x != f:
            total_num = total_num + [valid[x]]

    return total_num

    
#Purpose: calculates the centered average of the list
#Input: argument values
#Output: returns the average of list1
#Assumptions: Input for agrument are numbers
def centered_average (values):
    list1 = remove_num(values)
    sums = 0
    for charecter in list1:
        sums = sums + charecter

    if len(list1) == 0:
        return 0
    
    average = sums/len(list1)

    return average 


def centered_average_tester():
    
    if centered_average([1,2,3.5,4,"5"]) != 2.75:
        print('Fail test 1')
    if centered_average([-2,0,3,4,4,4]) != 2.75:
        print('Fail test 2')
    if centered_average(['0',1,1, 2,'2.45',3,4,4]) != 2.5:
        print('Fail test 3')
    if centered_average([1,8]) != 0:
        print('Fail test 4')
    if centered_average([2,'a','b'])!= 0:
        print('Fail test 5')



    



