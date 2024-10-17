

#Purpose: takes arguments ratio and n and returns the geometric sum
#Input: arguments ratio and n
#Output:returns the value assigned to ans
#Assumptions: arguments entered should be a positive number

def geometricsum (ratio, n):
    ans = 0
    for x in range (n+1):
        
        y = pow(ratio, x)
        
        ans = ans + y
       
    return ans 
print("Geometric sum is:", geometricsum(2,2))

#Test Cases
#Input: (2,2) Expected Output: 7
#Input: (1, 1000) expected output: 1001
#Input: (-2,2) expected output: 3
#Input: (-2,-2) expected output: 0
#Input:(2,0) expected output: 1

#Purpose: Takes in input from the user and prints the sum of those numbers
#Input: Argument n and inputs from user
#Output: The sum of the numbers get printed on screen
#Assumptions: Input should be a number 

def usersum (n):
    y = float(input("Enter first number:"))
    
    for rep in range(1, n):
        x = float(input("Enter next number:"))
       
        y = y + x 

    print("The sum of your entered values is", y)
    return y                                             

print(usersum(4))

#Test Cases
#Input: 10, 2.5, -5.7, 3 expeceted output: The sum of your entered values is 9.8    9.8
#Input: ten, 2,5, -5.7, 3 expected output: Value error
#Input: "10", 2.5, -5.7, 3 expected output: Value error
#Input: 2, -2, -2, -2 expected output: The sum of your entered values is -4
#Input: 100, -100, 100, -100 expected output: : The sum of your entered values is 0   0
#Input: 0,0,0,0 expected output: The sum of your entered values is 0   0
