from stack import Stack

#Purpose: Return true if symbols contains balanced parenthesis, false otherwise
#Input: a string with only parenthesis
#Ouput: True if balanced, False otherwise
#Assumptions: symbols only contains {,(,[,],),}
def balancedPars(symbols):
    a = Stack()
    for i in symbols:
        if i == '(' or i=='{' or i== '[':
            a.push(i)
        elif i == ')' or i=='}' or i== ']':
            s = a.pop()
            if matches(s,i) == False:
                return False
            
    

#Purpose: Return true start and end either(),[],or{} and false otherwise
#Input: start and end of a parenthesis
#Ouput: True if matching, false otherwise
#Assumptions: none
def matches(start, end):
    if start == '(' and end == ')':
        return True
    if start == '{' and end == '}':
        return True
    if start == '[' and end == ']':
        return True
    return False

if not balancedPars("(){[()[]](){()}}"):#expect true
    print("Error! Identified (){[()[]](){()}} as not balanced")

if not balancedPars("(){[}]"):#expect false
    print("Error! Identified (){[}] as balanced")
    
if balancedPars("(){[()[]](){}}({"):#expect false
    print("Error! Identified (){[()[]](){}}({ as balanced")

'''My son typed the input for this test case-
he doesn't know anything about python or stacks'''
print(balancedPars("))))))))"))#Expect: False
