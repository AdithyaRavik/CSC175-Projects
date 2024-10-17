import string
import random

#Purpose: prints the count of each letter appearing in the given string query
#Input: argument querry
#Output: Prints ,letter : count of the letter in string, on screen
#Assumptions: input for argument is a string
def freq (query):
    p = query
    ans = ""
    non_rep = ""

    for i in range(len(p)):
        x = p[i]
        if x not in ans and x != " " and x not in string.digits and x not in string.punctuation:
            non_rep = non_rep + x
        
        ans = ans + x
    
    for char in non_rep:
        
        y = p.count(char)
        print(char,":" ,y)

#Test Cases for freq(query)

#Input: "The weather is bad"
#Output:
#T : 1
#h : 2
#e : 3
#w : 1
#a : 2
#t : 1
#r : 1
#i : 1
#s : 1
#b : 1
#d : 1

#Input: "Whoo!!, It's -1!!"
#Output:
#W : 1
#h : 1
#o : 2
#I : 1
#t : 1
#s : 1

#Input: "There's 22? "
#Output:
#T : 1
#h : 1
#e : 2
#r : 1
#s : 1

#Input: hi  Output: Name error




#Purpose: Generates random key from lowercase alphabets 
#Inut: none
#Output: returns the random key
#Assumptions: none
def randkey():
    x = string.ascii_lowercase
   
   
   
    key = ''
    while len(key) < 26:
        rand = random.randint(0,25)
        
        
        while x[rand] in key:
            rand = random.randint(0,25)
        key = key + x[rand]

    
    return key 

def randkey_tester():
    key2 = randkey()

    if len(key2) < 26:
        print("Key lesser than 26 charecters")
    if len(key2) > 26:
        print('Key is greater than 26 charecters')

    for i in range(len(key2)):
        x = key2[i]
        
        if key2.count(x) > 1:
            print("Alphabet repeats in key")



