
#Purpose: opens the file and returns it
#Input: you input the file name and the command for what you want to do
#Output: returns the opened file
#Assumptions: input is a string
def open_file(name, command):
    aFile = open(name, command)
    return aFile

#Purpose: Converts data in file to a List
#Input: input is the opened file
#Output: returns the list with the data
#Assumptions: input is a List
def file_string(name):
    List = []
    for aline in name:
        List = List + [aline.split()]
        print(aline)
    List.sort()
    return List
print(file_string('Emma 3 John 4 Bill 2'))
#Purpose: converts list to a dictionary
#Input: two argments, one is for a list and the other if for a dictionary variable
#Output: the dictionary variable now holds the data from the list
#Assumptions: list should be a list and dict a dictionary 
def list_dict(List, Dict):
    for i in range(len(List)):
        print(i)
        if List [i][0] in Dict:
            Dict[List[i][0]] = Dict [List[i][0]] + int(List[i][1])
        else:
            Dict[List[i][0]] = int(List[i][1])

#Purpose: Finds the average based on hours worked by all employees
#Input: input is a dictionary
#Output: returns the value of the average
#Assumptions: input is a dictionary
def avghours (Dict):
    Hours = []
    for key in Dict:
        Hours += [Dict.get(key)]
    avg = sum(Hours)/len(Dict)
    return avg

#Purpose: Finds the maximum amount of hours worked by an employee
#Input: input is a dictionary
#Output: returns the maximum value
#Assumptions: input is a dictionary
def max_Dict(Dict):
    maxi = 0
    for key in Dict:
        if Dict.get(key) > maxi:
            maxi = Dict.get(key)
    return maxi

#Purpose: prints the hours worked and employee name on screen. It also denotes the employee who worked the maximum amount of hours and average amount of hours
#Input: has 3 arguments, one takes the dictionray, second takes average hrs worked value and third takes maximum hrs worked value
#Output: prints hours worked and employee names on screen. It also uses asterisks which denote infomration.
#Assumptions: input for dictionary is a dictionary and that average and maximum values are a number
def print_result(Dictionary, avg, maxi):
    for i in Dictionary:
        if Dictionary[i] == maxi:
            print('**' , i,Dictionary[i])
        elif Dictionary[i] >= avg:
            print('*', i,Dictionary[i])
        else:
            print(i,Dictionary[i])


#Purpose: call on all the previous functions to accompish the task
#Input: none
#Output: prints hours worked and employee names on screen with asterisks which denote information
#Assumptions: none
def main():
    Dictionary = {}
    List = file_string(open_file('hrsworked.txt', 'r'))
  
    list_dict(List, Dictionary)
    
    avg = avghours(Dictionary)
  
    m = max_Dict(Dictionary)

    print_result(Dictionary, avg, m)

    

main()

#Test Cases

#Input : John 4  Brad 4  Joe 7  Emily 2  Mr.P 1  Emily 3  John 1

#Expected Output: Brad 4  *Emily 5   **Joe 7   *John 5   Mr.P 1

#Input: Bill 0  Kate 9  Oly 6  Nio  2   Ben  4  Nio 3   Kate 1   Nio 3

#Expected Output: Ben 4  Bill 0  **Kate 10  *Nio 8  *Oly 6



