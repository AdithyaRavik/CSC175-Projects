#Purpose: Reads a file into a list of sublists
#Input: Takes a file name as an argument
#Ouput: Returns the list it has generated
#Assumptions: Assumes the file named exists in the same folder as this program
def fileToList(file):
    List = []
    f = open(file, "r")
    for aline in f:
        List += [aline.split()]
    List.sort()
    return List



#Purpose: Converts a list of sublists into a dictionary, adds up values for repeat keys
#Input: Takes a list and a dictionary as arguments
#Output: Directly edits the dictionary it was passed
#Assumptions: Assumes the List contains only sublists of length 2
#             Assumes the first index in each sublist contains a str
#             Assumes the second index in each sublist an int
def listToDict(List, Dict):
    for i in range(len(List)):
        if List[i][0] in Dict:
            Dict[List[i][0]] += int(List[i][1]) 
        else:
            Dict[List[i][0]] = int(List[i][1])



#Purpose: Returns the avg number of hours worked
#Input: Takes the name of your dictionary as an argument
#Output: Returns the avg: a float
#Assumptions: Assumes at least one entry in the dictionary
#             Assumes the dictionary keys are only ints (would work for floats too)
def avgHours(Dict):
    Hours = []
    for key in Dict:
        Hours += [Dict.get(key)]
    avg = sum(Hours)/len(Dict)
    return avg

  

#Purpose: Returns the max value of all values in the given dictionary
#Input: It is passed a dictionary to search as the argument
#Ouput: It returns the max value
#Assumptions: Assumes all the values are numbers
def maxDictVal(Dict):
    m = 0
    for key in Dict:
        if Dict.get(key) > m:
            m = Dict.get(key)
    return m


        
def Print(Dict,avg):
    return 0




def main():
    Dictionary = {}
    List = fileToList('hrsworked.txt')
    print(List)
    listToDict(List, Dictionary)
    print(Dictionary)
    avg = avgHours(Dictionary)
    print(avg)
    m = maxDictVal(Dictionary)
    print(m)

main()
