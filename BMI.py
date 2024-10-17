#purpose: Prompt user with a question and get their response.
#inputs: prompt - what to display to the user
#output: Return what user enters.
#assumptions: none
def getUserInput(prompt):
    response = input(prompt)
    return response

#purpose: Validate that a number is in range [lower,upper].
#inputs: arguments are:
#           --input a number that needs to be validated
#           --lower and upper limits
#Output: Returns True if lower<=input<=upper. Otherwise, returns False.
#assumptions: input, lower and upper are numbers
def isInputInRange(input, lower, upper):
    if input >= lower and input <= upper:
        return True
    else:
        return False

def isInputInRange_test():
    if isInputInRange(50, 1, 100) != True:
        print("Fail Test 1")
    if isInputInRange(110, 1, 100) != False:
        print("Fail test 2")

#purpose: Obtain a number from user between range [lo,hi].
#inputs: prompt- question to ask the user
#        convertfunc- function to convert user's response to a number 
#        lo and hi- describes the range of valid responses
#output: returns user input if between lo and hi, otherwise returns None
#assumptions: lo and hi are numbers, user's response is compatible with convertfunc
def getValidNumberInput(prompt, convertfunc, lo, hi):
    value = convertfunc(getUserInput(prompt))
    if not isInputInRange(value, lo, hi):
         print("Value not in range [" + str(lo) +"," + str(hi) + "]")
    else:
        return value

#Purpose: Determine weight category
# Input: argmunet bmi
# Output: Weight category returned as string
# Assumptions: Assume bmi is a number and in range
def getBMICategory(bmi):
    if bmi < 18.5 :
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return"Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def getBMICategory_test():
    if getBMICategory(15) != 'Underweight':
        print("Fail Test 1")
    if getBMICategory(20) != 'Normal':
        print("Fail Test 2")
    if getBMICategory(28) != 'Overweight':
        print("Fail Test 3")
    if getBMICategory(50) != 'Obese':
        print('Fail Test 4')

def main():
    Aheight =getValidNumberInput("Enter populations average height in inches: ", float, 1, 100)
    Aweight= getValidNumberInput("Enter populations average weight in pounds: ", float, 1, 1000)

    BMI = Aweight / Aheight ** 2 * 703

    print("BMI:", BMI, " Category:", getBMICategory(BMI))
