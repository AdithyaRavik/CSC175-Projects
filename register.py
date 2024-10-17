#-----------------------------------------------------------------------
#Purpose= calculates change in quarters, dimes, nickels, and pennies
#Input = the change in numbers
#Output= prints the change on screen in quarters, dimes, nickels, and pennies
#Assumptions = Input must be a positive integer
#Program fails if input is string(words), negative int, or float.
#-----------------------------------------------------------------------


#Quarters = 25 cents
#Dimes = 10 cents
#Nickels = 5 cents
#Pennies= 1 cent

x = int(input("What amount of change would you like to make?")) # Ex) Change = 87
                      
quarters = x // 25 # quarters = 87 // 25 =3 

cal_quarters = x -(25  * quarters) # change remaining = 87 -(25 * 3) = 12

dimes = cal_quarters // 10 # dimes= 12 / 10 = 1 

cal_dimes = cal_quarters - (10 * dimes) # change remaining = 12-(10*1) = 2

nickels = cal_dimes // 5 # nickels = 2 // 5= 0

cal_nickels = cal_dimes - (5 * nickels) # change remaining = 2 - ( 5*0) = 2

pennies = cal_nickels // 1 # pennies = 2

cal_pennies = cal_nickels - (1 * pennies) # change remaining = 2 -( 1*2) = 0

print( "Results are", quarters, "Quarters", dimes, "Dimes", nickels, "Nickels", pennies, "Pennies")

#TEST CASES 
# input: 89  Expected output: Results are 3 Quarters 1 Dimes 0 Nickels 4 Pennies
# input: -89 Expected output: Results are -4 Quarters 1 Dimes 0 Nickels 1 Pennies
# input: eighty nine Expected output: runtime error
# input: 89.5 Expected output: runtime error
# input: 259 Expected output: Results are 10 Quarters 0 Dimes 1 Nickels 4 Pennies

#Limitations

#a) The program will give a wrong input if you type in a negative number.
# It will result in a Semantic error. You could convert the negative number to a positive.
#Or you have to change the equation to accomidate a negative number.

#b) Line 15 shows error message. This is because entering a str results in runtime error.
