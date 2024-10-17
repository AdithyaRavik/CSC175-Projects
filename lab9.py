#Purpose: Takes in arguments and returns a string made of n repetitions of the last n characters of the string
#Input: Arguments string and n
#Output: returns value of b or (b*n)
#Assumptions: Value entered for string is a string
def repeatEnd (string, n):
    a = string
    length = len(a)
    b = ""
    
    if n <= 0 or n >= length:
        return  b
    
    b = (a[-n:])
    return (b * n)

#Purpose: tester function for repeatEnd()
#Input: none
#Output: none
#Assumptions: tests do not fail 
def repeatEnd_tester():
    if repeatEnd("Hello",2) != "lolo":
        print ("Test 1 fail")
    if repeatEnd("Hello",10) != "":
        print("Test 2 fail")
    if repeatEnd("Hello", -2) != "":
        print("Test 3 fail")
        

#Purpose: takes in arguemnt and returns the count of the number of triples in the string
#Input: Argument string2
#Output: returns value of ans
#Assumptions: Value entered for string2 is a string 
def countTripple (string2):
    c = string2
    length2 = len(c)

    ans = 0
    for i in range (length2-2):
        if c[i] == c[i+1] == c[i+2]:
            ans = ans + 1

    return ans    

#Purpose: tester function for countTripple()
#Input: none
#Output:none
#Assumptions: tests do not fail 
def countTripple_tester():
    if countTripple("abcd") != 0:
        print("Test 1 fail")
    if countTripple("abxxxcd") != 1:
        print("Test 2 fail")
    if countTripple("abxxxcdyyyy") != 3:
        print("Test 3 fail")


    




    
    
