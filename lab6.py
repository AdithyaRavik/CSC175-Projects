
import random

#Purpose: It generates random number between 1 to 20 and prints our "You Win!" or "You Lose!" depending on certain conditions
#Input: None
#Output: prints out "You Win!" or "You Lose!" on to the screen depending on certain conditions
#Assumptions: none

def chance():

    num1 = random.randrange(1,20)
    num2 = random.randrange(1,20)
    num3 = random.randrange(1,20)
   

    if num1 ==13 or num2 == 13 or num3 == 13:
            print("You Lose")
    elif num1 != num2 != num3 != num1:
        print("You Win!")
    else:
        print("You Lose!")

print(chance())

#Purpose: Takes in argument a and b and returns variable closest to 21 if certain conditions are met
#Input: Arguments a and b
#Output: returns variable closest to 21 if certain conditions are met
#Assumptions: values entered for the argument should be a positive number

def blackjack(a , b):
    
    if a > 21 and b > 21:
        return 0
    if a > 21:
        return b
    if b > 21:
        return a

    if a > b:
        return a
    else:
        return b
    

print(blackjack(4,-5.5))

def blackjack_tester():
    if blackjack(24, 23) != 0:
        print("Error test case#1")
    if blackjack(22,15) != 15 :
        print("Error test case#2")
    if blackjack (15,22) != 15:
        print("Error test case#3")
    if blackjack(21,15) != 21:
        print("Error test case#4")
    if blackjack(15,21) != 21:
        print("Error test case#5")
    if blackjack(16,16) != 16:
        print("Error test case#6")

blackjack_tester()
    
