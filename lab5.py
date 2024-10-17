
#Purpose: prints odd numbers up to the limit given by the argument 
#Input: argument limit
#Output: prints odd numbers on the screen up to the limit
#Assumptions: argument must be an positive integer and preferebly not equal to 0 

def odd (limit):
    for x in range(1, limit + 1, 2):
        print(x)
#Test cases
# Input: 3 expected output: 1, 3
# Input: 4 expected output : 1, 3
# Input: 0 expected output: blank
#Input: -4 expected output: blank
#Input: 4.5 expected output: type error
#Input:     expected outut: type error

#Purpose: Does a countdown with the value given by the argument
#Input: argument n
#Output: displays countdown on screen and the word blastoff at the end
#Assumptions: Number must be an positive integer and preferebly not equal to 0

def blastoff(n):
    for cal in range (n):
        print(n -1 * cal, "...", )

    print("blastoff!") 

#Test cases
# Input: 5 expected output: 5.. 4... 3... 2... 1... blastoff!
# Input: 0 expected output: blastoff!
#Input: -3 expected output: blastoff!
#Input: 4.5 expected output: type error
#Input: "3" expected output: type error
#Input:     expected output: type error 
