
import random 

#Purpose: Rolls dice and returns random value between 1 and n
#Input: argument n
#Output: returns random value
#Assumptions: none
def roll (n):
    n = int(n)
    dice = random.randint(1, n)
    return dice


#Purpose: Calculates score based on certain conditions
#Input: arguments r1, r2, and s
#Output: returns value of score
#Assumptions: none
def scoreRound (r1, r2, s):
    score = r1 + r2

    if r1 == r2 and r1 != s and r2 != s:
        score = score + 5
    elif r1 == r2 == s == r1:
        score = score - 3*s
    else:
        return score

    return score 


#Purpose: Tests scoreRound() function
#Input: none
#Output: none, if tests do not fail
#Assumptions: tests won't fail
def test_scoreRound():
    if scoreRound(3,3, 4) != 11:
        print("Fail test 1")
    elif scoreRound(3,3,3) != -3:
        print("Fail test 2")
    elif scoreRound (2,4,4) != 6:
        print("Fail Test 3")
    elif scoreRound(2,4,6) != 6:
        print("Fail test 4")


#Purpose: Returns total score based on rounds played and dice sides
#Calls functions roll() and scoreRound()
#Input: arguments rounds and sides
#Output: returns value of total_score
#Assumptions: none
def play(rounds, sides):
    total_score = 0

    for x in range (rounds):
        play1 = roll(sides)
        play2 = roll(sides)
        play_score = scoreRound(play1, play2, sides)
        total_score = total_score + play_score
        print("Rolled ", play1, play2, "Scoring:", play_score)
    return total_score

#Purpose: Displays how you did based on your score and the goal
#Input: arguments goal and score
#Output: prints rn on screen and returns rn
#Assumptions: none
def result(goal, score):

    print("Total Score: ", score )

    if score >= goal * 2:
        rn = ("Nailed it!")
    elif score > goal and score < goal * 2:
        rn = ("So so performance")
    elif score < goal:
        rn = ("Not good... not good at all!")

    print(rn)
    return rn
    

#Purpose: tests function result()
#Input: none
#Output: prints the score and message on screen for each test case but does not print "fail case"
#Assusmptions: tests do not fail
def test_result():

    if result(2,4) != "Nailed it!":
        print("test 1 fail")
    elif result (4,5) != "So so performance":
        print("test 2 fail")
    elif result(4,2) != "Not good... not good at all!":
        print("test 3 fail")

   
#Purpose: Calls functions and executes code necessary to play the game
#Input: Asks for input from the user twice
#Output: Prints the goal, dice rolls, total score, and how you did,etc, on screen
#Assumptions: input is a positive integer, != 0
def main ():
    print("Welcome to the dice game!")
    dice_sides= int(input("What sided die would you like to use? : "))
    num_rounds = int(input("How many rounds would you like to play? :"))

    goal_main = num_rounds * (dice_sides + 1) / 2
    print("Your goal is to earn ", goal_main, "total points in ", num_rounds, "rounds.")

    x = play(num_rounds, dice_sides)
    result(goal_main, x)

main()
    
    
    


    









